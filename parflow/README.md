# ParFlow

This directory aims to capture the various work done around parflow.
In the following command we would assume $ROOT to be the path to the root of that repository.

## Installing ParaFlow on Ubuntu 18.04 or 20.04

```
mkdir tmp
cd tmp
sudo $ROOT/parflow/scripts/01_packages.sh
./$ROOT/parflow/scripts/02_parflow.sh
```

## Installing ParFlow in an Ubuntu docker

Here is the various set of ways you can build an ubuntu image with Parflow


__Ubuntu 18.04__ Hypre-2.19.0 + Parflow-3.6.0

```
cd $ROOT/paraflow
docker build                          \
  --build-arg BASE_IMAGE=ubuntu:18.04 \
  -c ./docker/development/Dockerfile  \
  -t ubuntu-18-hypre-2.19-parflow-3.6
```

__Ubuntu 20.04__ Hypre-2.19.0 + Parflow-3.6.0

```
cd $ROOT/paraflow
docker build                          \
  --build-arg BASE_IMAGE=ubuntu:20.04 \
  --build-arg HYPRE_VERSION=v2.19.0   \
  --build-arg PARFLOW_VERSION=v3.6.0  \
  -c ./docker/development/Dockerfile  \
  -t ubuntu-18-hypre-2.19-parflow-3.6
```

__Ubuntu 20.04__ with Parflow and Hypre on __master__

```
cd $ROOT/paraflow
docker build                          \
  --build-arg BASE_IMAGE=ubuntu:20.04 \
  --build-arg HYPRE_VERSION=master    \
  --build-arg PARFLOW_VERSION=master  \
  -c ./docker/development/Dockerfile  \
  -t ubuntu-18-hypre-master-parflow-master
```

## Installing ParFlow on macOS

```
mkdir tmp
cd tmp
CMAKE_TYPE=cmake-3.17.2-Darwin-x86_64.tar.gz && ./$ROOT/parflow/scripts/02_parflow.sh
```
