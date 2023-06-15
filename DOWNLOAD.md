Dataset **Photometric stereo leafs** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/E/A/rw/ZmdhfjcllHYVzZHe7gdj1Z7TUrXbQ4dDHKERzW3NuUEngo3Us5PtELr1DonYpz05fjfkHSEv9UCauxIdtTQ31DemzAaTqapPSMgku69c3H5UwkIrQpUITDbZeB99.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Photometric stereo leafs', dst_path='~/dtools/datasets/Photometric stereo leafs.tar')
```
The data in original format can be 🔗[downloaded here](https://datashare.ed.ac.uk/bitstream/handle/10283/3280/PS%20Plant%20training%20data%20set.zip?sequence=4&isAllowed=y)