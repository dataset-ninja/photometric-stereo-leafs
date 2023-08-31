# https://datashare.ed.ac.uk/handle/10283/3280
# https://datashare.ed.ac.uk/handle/10283/3279

import csv
import glob
import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Photometric stereo leafs"

    train_images_folder = (
        "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3280/PS Plant training data set"
    )
    train_subfolders = [
        "Albedo images",
        "Composite images",
        "Foreground_Background images",
        "Grayscale images",
        "Shadow images",
        "Surface normal map images",
    ]
    train_masks_folder = "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3280/PS Plant training data set/Ground truth (leaf labels)"
    test_images_folder = "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3279/PS-Plant test data set/4. Masks and cropped albedo_grayscale_composite"
    test_subfolders = ["Binary masks", "CroppedAlbedo", "CroppedComposite", "CroppedGrayscale"]
    test_masks_folder = "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3279/PS-Plant test data set/6. Segmented"
    test_tag_data_path = "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3279/PS-Plant test data set/PS-Plant test data set-masks_metadata.csv"
    train_tag_data_path = "/mnt/d/datasetninja/photometric-stereo-leafs/DS_10283_3280/PS-Plant_training_data_set-metadata.csv"

    batch_size = 30
    image_suffix = "grayscale"
    train_mask_suffix = "label"
    test_mask_suffix = "mask"
    images_ext = ".png"
    group_tag_name = "im_id"

    ds_to_folders = {
        "test": (
            test_images_folder,
            test_masks_folder,
            test_mask_suffix,
            test_tag_data_path,
            test_subfolders,
        ),
        "train": (
            train_images_folder,
            train_masks_folder,
            train_mask_suffix,
            train_tag_data_path,
            train_subfolders,
        ),
    }

    tag_subfolder_names = test_subfolders + train_subfolders
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_subfolder_names]

    def get_unique_colors(img):
        unique_colors = []
        img = img.astype(np.int32)
        h, w = img.shape[:2]
        colhash = img[:, :, 0] * 256 * 256 + img[:, :, 1] * 256 + img[:, :, 2]
        unq, unq_inv, unq_cnt = np.unique(colhash, return_inverse=True, return_counts=True)
        indxs = np.split(np.argsort(unq_inv), np.cumsum(unq_cnt[:-1]))
        col2indx = {unq[i]: indxs[i][0] for i in range(len(unq))}
        for col, indx in col2indx.items():
            if col != 0:
                unique_colors.append((col // (256**2), (col // 256) % 256, col % 256))

        return unique_colors

    def create_ann(image_path):
        labels = []
        tags = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        im_name = get_file_name(image_path)
        image_suffix = im_name.split("_")[-1]
        image_name = im_name.rstrip(image_suffix)
        id_data = image_name[:-1]
        group_id = sly.Tag(tag_id, value=id_data)
        if ds_name == "train":
            plant_number_data = int(id_data[-1])
        else:
            plant_number_data = int(id_data[0])
        plant_number = sly.Tag(tag_plant_number, value=plant_number_data)
        tags.extend([group_id, plant_number])
        mask_name = image_name + mask_suffix + images_ext
        if ds_name == "test":
            subfolder = image_path.split("/")[-2]
            if subfolder == "Binary masks":
                subfolder = "Plant {}".format(plant_number_data)
            mask_path = os.path.join(masks_path, subfolder, mask_name)
        else:
            mask_path = os.path.join(masks_path, mask_name)

        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)
            unique_colors = get_unique_colors(mask_np)
            for color in unique_colors:
                mask = np.all(mask_np == color, axis=2)
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    curr_bitmap = sly.Bitmap(obj_mask)
                    curr_label = sly.Label(curr_bitmap, obj_class)
                    labels.append(curr_label)

        if ds_name == "test":
            tag_data = image_name_to_tags[mask_name]
            lights = sly.Tag(tag_lights, value=tag_data[5])
            tags.append(lights)

        else:
            tag_data = image_name_to_tags[image_name[:-1]]
            number = sly.Tag(tag_number, value=int(tag_data[0]))
            tags.append(number)

        temperature = sly.Tag(tag_temperature, value=int(tag_data[0]))
        intensity = sly.Tag(tag_intensity, value=int(tag_data[1]))
        interval = sly.Tag(tag_interval, value=float(tag_data[2]))
        germination = sly.Tag(tag_germination, value=int(tag_data[3]))
        interest = sly.Tag(tag_interest, value=tag_data[4])

        tags.extend([temperature, intensity, interval, germination, interest])

        if "Plant" in image_path.split("/")[-2]:
            tag_subfolder_name = image_path.split("/")[-3]
        else:
            tag_subfolder_name = image_path.split("/")[-2]
        tags.extend(
            [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == tag_subfolder_name]
        )

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("leaf", sly.Bitmap)

    tag_number = sly.TagMeta("leaf number", sly.TagValueType.ANY_NUMBER)
    tag_temperature = sly.TagMeta("growth temperature", sly.TagValueType.ANY_NUMBER)
    tag_intensity = sly.TagMeta("growth light intensity", sly.TagValueType.ANY_NUMBER)
    tag_interval = sly.TagMeta("interval between imaging", sly.TagValueType.ANY_NUMBER)
    tag_germination = sly.TagMeta("days after germination", sly.TagValueType.ANY_NUMBER)
    tag_interest = sly.TagMeta("region of interest", sly.TagValueType.ANY_STRING)
    tag_lights = sly.TagMeta("lights", sly.TagValueType.ONEOF_STRING, possible_values=["on", "off"])
    tag_plant_number = sly.TagMeta("plant number", sly.TagValueType.ANY_NUMBER)
    tag_id = sly.TagMeta("im_id", sly.TagValueType.ANY_STRING)

    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=tag_metas
        + [
            tag_number,
            tag_temperature,
            tag_intensity,
            tag_interval,
            tag_germination,
            tag_interest,
            tag_lights,
            tag_plant_number,
        ],
    )

    meta = meta.add_tag_meta(group_tag_meta)
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    for ds_name in list(ds_to_folders.keys()):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_path = ds_to_folders[ds_name][0]
        masks_path = ds_to_folders[ds_name][1]
        mask_suffix = ds_to_folders[ds_name][2]
        tags_data_path = ds_to_folders[ds_name][3]
        images_subfolder = ds_to_folders[ds_name][4]

        image_name_to_tags = {}

        with open(tags_data_path, "rb") as f:
            content = f.read().decode("utf-8", errors="replace").split("\n")
            for idx, row in enumerate(content):
                if idx in [0, 1]:
                    continue
                row = row.replace('"', "")
                if len(row) != 0:
                    row = row.replace(" ", "")
                    data = row.split(",")
                    interest_regoin = " ".join(data[6:10])
                    image_name_to_tags[data[0]] = data[1:5] + [interest_regoin] + [data[10]]

        for curr_images_subfolder in images_subfolder:
            curr_images_path = os.path.join(images_path, curr_images_subfolder)

            if ds_name == "test":
                if curr_images_subfolder == "Binary masks":
                    images_pathes = glob.glob(curr_images_path + "/*.png")
                else:
                    images_pathes = glob.glob(curr_images_path + "/*/*.png")
            else:
                images_pathes = [
                    os.path.join(curr_images_path, im_name)
                    for im_name in os.listdir(curr_images_path)
                ]

            progress = sly.Progress(
                "Create dataset {}, add {} data".format(ds_name, curr_images_subfolder),
                len(images_pathes),
            )

            for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
                img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(img_names_batch))
    return project
