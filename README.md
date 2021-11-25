# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

*This is a forked repo from https://github.com/cianmscannell/cardisort*

## Installation

### Setting up the working directory

Assume the data is located in this directory: `/home/user/data/`

1. Clone this repository

```bash
$ git clone https://github.com/avansp/cardisort.git
```

2. Copy the pre-trained model weights from [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh) to `/home/user/data/cardisort_model.ckpt`

3. Let's say you have a CMR study folder called `CMR-Study`. Copy the folder into `/home/user/data/images/CMR-Study`


### Docker setup

1. Build a docker image:

```shell
$ docker build -t cardisort .
```

2. Run a container and specify the data folder to be mapped into the container:

```shell
$ ./docker_run.sh --data /home/user/data
```

See more options with `./docker_run.sh --help`

3. You will be in the container shell in the `/app` folder. The codes are in `/app/codes` and your data folder is in `/app/data` folder.


## Usage

1. Create result directory
```bash
$ mkdir /app/data/results
```

2. Run the cardisort
```bash
$ cd /app/codes
$ python cardisort_inference_2.py /app/data/cardisort_model.ckpt /app/data/images/CMR-Study /app/data/results
```

**Some Notes**

1. Your working directory in the container is `/app`
2. You're nameless, but your user/group id's (UID & GID) in the container will match with your host UID & GID. 
3. The container is deleted when you exit from the container shell.

## References

If you find this code helpful in your research please cite the following [paper](https://arxiv.org/abs/2109.08479):

Ruth P Lim, Stefan Kachel, Adriana DM Villa, Leighton Kearney, Nuno Bettencourt, Alistair A Young, Amedeo Chiribiri, and Cian M Scannell. CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images. arXiv preprint arXiv:2109.08479, 2021.

```
@misc{lim2021cardisort,
      title={CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images}, 
      author={Ruth P Lim and Stefan Kachel and Adriana DM Villa and Leighton Kearney and Nuno Bettencourt and Alistair A Young and Amedeo Chiribiri and Cian M Scannell},
      year={2021},
      eprint={2109.08479},
      archivePrefix={arXiv},
      primaryClass={eess.IV}
}
```
