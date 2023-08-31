The authors of the *Photometric Stereo Leafs* dataset recognized the necessity for accurate and quantitative methods to predict plant growth in dynamic natural environments, a crucial requirement in the face of changing global climate and increasing population. They highlighted the significance of computer vision in driving advancements in plant phenotyping for both research and agriculture applications. To this end, the authors focused on developing imaging technologies for comprehensive plant growth assessment.

A strong indicator of plant yield is above-ground growth, particularly 3D imaging of vegetative growth, which has garnered substantial attention in phenotyping research. They distinguished between passive and active 3D imaging approaches for plant architecture. Passive methods capture plant structures without introducing new energy, employing techniques like multi-view stereo, structure from motion, and light-field cameras. Active 3D imaging methods, like structured light and laser scanners, emit energy to overcome challenges faced by passive methods. Despite the improvements offered by both passive and active 3D imaging, existing techniques still lack in various crucial aspects such as speed, portability, spatial resolution, and cost-effectiveness.

The authors then introduced the concept of photometric stereo (PS), an active imaging technique that offers high image resolutions and rapid capture speeds at a low cost. This technique relies on capturing images under controlled, varied, and directional illumination to generate dense surface normal maps. They noted its potential for encoding complex 3D morphology, essential for recognizing and quantifying growth patterns. The authors presented their novel imaging system called *PS-Plant*, which leverages photometric stereo to monitor the growth and development of Arabidopsis in three dimensions.

The dataset comprises 21 `<i>`Arabidopsis thaliana `</i>` (L. Heynh. Col-0, wild type) plants grown in a growth cabinet at 22&deg; under 150 µmol photons m ^-2^ s ^-1^ in 12/12 hr light/dark cycles. The dataset represents plants at varying time intervals (12 to 48 hours) from 11 and 24 days after germination.

Each Arabidopsis plant from the raw data was individually cropped by specifying the rosette centroid location and the size of the region of interest. All crops have the same resolution (650x560 pixels). The cropped images were named as the parent directory with a <i>_X</i> suffix, where <i>X</i> is the plant number in the tray. The images provided are:

* Annotated image layers: Individual leaf labels for each plant were manually generated using Adobe Photoshop CS6 (Adobe Systems, CA, USA). Every leaf mask was stored in a separate layer in the format of <i>Leaf No</i>. If the leaf was not visible due to occlusions, an empty layer was included with a title of the missing leaf number. Annotated image layers were stored in a <i>psd</i> file format.
* Ground truth (leaf labels) images: *.png* images generated from the *.psd* files (B)
* ***Albedo images***  (C)
* ***Surface normal map images*** (D)
* ***Grayscale images***: mean of various illumination directions (E)
* ***Shadow images*** (F)
* ***Composite images***: normals in x and y directions, and albedo (G)
* ***Foreground_Background images***: a foreground (white) and background (black) image mask (H).

<img src="https://github.com/supervisely/supervisely/assets/78355358/66f77a5f-d58c-4640-8920-31135a011818" alt="image" width="800">
