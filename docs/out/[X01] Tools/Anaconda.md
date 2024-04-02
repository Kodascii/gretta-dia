<link rel="stylesheet" href="../../stylesheet.css">

# Anaconda

## Setups

### CREATE ENV

```sh
$ conda create --name <env_name> python=3.8
```

### ACTIVATE

```sh
$ conda activate <env_name>
```

### INIT SHELL

```sh
$ conda init 
```

> It sets up the shell configuration files to include conda's functionality, making it easier to use conda commands directly in your command prompt or terminal.


### INSTALL PACKAGE

```sh
$ conda install <pkg>
```

## Extras

### DELETE ENVIRONMENT
```sh
$ conda remove --name <env_name> --all
```

### UPDATE CONDA
```sh
conda update -n base -c defaults conda
```