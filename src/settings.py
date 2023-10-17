from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Photometric Stereo Leafs"
PROJECT_NAME_FULL: Optional[str] = "Photometric Stereo Training Data Set with Annotated Leaf Masks"
HIDE_DATASET = False  # set False when 100% sure about repo quality
##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Biological(), Research.Genetic()]
CATEGORY: Category = Category.Biology(extra=Category.Agriculture())

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2019-03-25"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://datashare.ed.ac.uk/handle/10283/3199"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2660736
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/photometric-stereo-leafs"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Photometric stereo training data set with annotated leaf masks": "https://datashare.ed.ac.uk/download/DS_10283_3280.zip",
    "Photometric stereo test data set": "https://datashare.ed.ac.uk/download/DS_10283_3279.zip",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = {
    "Research paper": "https://academic.oup.com/gigascience/article/8/5/giz056/5498634?login=false",
    "Dataset Description": "https://datashare.ed.ac.uk/bitstream/handle/10283/3280/PS-Plant%20training%20data%20set%20description.pdf?sequence=3&isAllowed=y",
}
CITATION_URL: Optional[str] = "https://datashare.ed.ac.uk/handle/10283/3280"
AUTHORS: Optional[List[str]] = ["Scorza, Livia", "Bernotas, Gytis", "McCormick, Alistair"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "University of Edinburgh, Scotland"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.ed.ac.uk/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__PRETEXT__": "Decomposed multi-channel *train* images are grouped by unique ***im_id*** into 221 groups with 6 layers each: ***Albedo images***, ***Surface normal map images***, ***Grayscale images***, ***Shadow images***, ***Composite images***, and ***Foreground_Background images***",
    "test images layers": [
        "Binary masks",
        "CroppedAlbedo",
        "CroppedComposite",
        "CroppedGrayscale",
    ],
    "__POSTTEXT__": "Additionally, images metadata contains information about ***leaf number***, ***plant number***, ***lights***, ***region of interest***, ***days after germination***,***interval between imaging***, ***growth light intensity***, ***growth temperature***, and the ***growth light intensity***",
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
