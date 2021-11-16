# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

*This is a forked repo from https://github.com/cianmscannell/cardisort*

## Using docker

### Building from `Dockerfile` for development

To build from the `Dockerfile`, call this in the project directory:

```shell
$ docker build -t cardisort .
```

Then run a container using all GPU's with interactive shell:

```shell
$ docker run --gpus all -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 
--user $(id -u):$(id -g) --name cardisort -v [LOCALDIR]:/app cardisort
```

where `[LOCALDIR]` is a host directory (absolute path) that contains also this project. You may want to include data file.

E.g. suppose your directory is as follows:

```
/path/to
  |
  /my_folder
    |
    /cardisort
        |
        Dockerfile
        ...
    /image-data
    ...
```

Then you can run the container as:

```shell
$ docker run --gpus all -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
--user $(id -u):$(id -g) --name cardisort -v /path/to/my_folder:/app cardisort
```

Notes:

1. Your working directory in the container is `/app`
2. The base image has also `/workspace` folder that you can use.
3. You're nameless, but your user/group id's (UID & GID) in the container will match with your host UID & GID.
4. The container is not deleted when you exit from the container shell.

   To delete the container you can call:
   ```shell
   $ docker container rm cardisort
   ```

5. When you exit, the container is stopped. You can start and enter the shell again using:

   ```shell
   $ docker container start -i cardisort
   ```

###    

---

This is a deep learning network which was developed to sort cardiac MRI images by sequence type and imaging plane, facilitating efficient and fully automated post-processing pipelines.

Please find the pre-trained model weights [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh).

The model can be run to sort a folder of DICOM images as:

    >> python cardisort_inference.py [INPUT_FOLDER] 
or    

    >> python cardisort_inference.py [INPUT_FOLDER] [OUTPUT_FOLDER]


If you find this code helpful in your research please cite the following paper:
```
@article{lim2021cardisort,
  title={CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images},
  author={Lim, Ruth P, and Kachel, Stefan, and Villa, Adriana DM, and Kearney, Leighton, and Bettencourt, Nuno, and Young, Alistair A, and Chiribiri, Amedeo,  and Scannell, Cian M},
  year={under review}
}
```
