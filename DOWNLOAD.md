Dataset **Photometric Stereo Leafs** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/m/T/vY/6mpZqRAu3fbOMY09vDrfVEGs5Cz6bWE9ATiOPxyrFo3CG04KWZpdmzghOjWGFm1LWbJf9S8nPMleJayVegclkbHV7bnchm6b5cr3is8gJiwS3fMjmDHTFPx50kFT.tar)

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
