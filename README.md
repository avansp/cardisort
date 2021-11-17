# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

*This is a forked repo from https://github.com/cianmscannell/cardisort*

## Installation

### Setting up the working directory

Assume that you are working from this folder: `/home/user/cardisort-test/`

1. Clone this repository

```bash
$ git clone https://github.com/avansp/cardisort.git
```

2. Copy the pre-trained model weights from [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh) to `/home/user/cardisort-test/cardisort_model.ckpt`

3. Let's say you have a CMR study folder called `CMR-Study`. Copy the folder into `/home/user/cardisort-test/images/CMR-Study`


### Docker setup

1. Build a docker image from the `Dockerfile`:

From the working folder `/home/user/cardisort-test/`
```shell
$ cd cardisort
$ docker build -t cardisort .
```

2. Run a container using all GPU's with interactive shell:

```shell
$ docker run --gpus all -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \ 
--user $(id -u):$(id -g) --name cardisort -v /home/user/cardisort-test:/app cardisort
```

3. You will be in the container shell in the `/app` folder. You can run the cardisort application as:

```bash
$ mkdir results
$ cd cardisort
$ python cardisort_inference_2.py ../cardisort_model.ckpt ../images/CMR-Study ../results
```

## Some Notes

1. Your working directory in the container is `/app`
2. You're nameless, but your user/group id's (UID & GID) in the container will match with your host UID & GID. 
3. The container is not deleted when you exit from the container shell.

   To delete the container you can call:
   ```shell
   $ docker container rm cardisort
   ```
   
4. When you exit, the container is stopped. You can start and enter the shell again using:

   ```shell
   $ docker container start -i cardisort
   ```

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

If you find this code helpful in your research please cite the following paper:
```
@article{lim2021cardisort,
  title={CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images},
  author={Lim, Ruth P, and Kachel, Stefan, and Villa, Adriana DM, and Kearney, Leighton, and Bettencourt, Nuno, and Young, Alistair A, and Chiribiri, Amedeo,  and Scannell, Cian M},
  year={under review}
}
```
