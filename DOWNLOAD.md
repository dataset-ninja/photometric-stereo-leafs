Dataset **Photometric Stereo Leafs** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE4NDlfUGhvdG9tZXRyaWMgU3RlcmVvIExlYWZzL3Bob3RvbWV0cmljLXN0ZXJlby1sZWFmcy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJHb2RRc21aQmFKdWN0NEgzVnM1VlVid2RrSXdoQnBxRE9rNGI5S1MwT2Q0PSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Photometric Stereo Leafs', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Photometric stereo training data set with annotated leaf masks](https://datashare.ed.ac.uk/download/DS_10283_3280.zip)
- [Photometric stereo test data set](https://datashare.ed.ac.uk/download/DS_10283_3279.zip)
