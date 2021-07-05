# This is a basic workflow to help you get started with Actions

name: Docker Build and Push

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      -
        name: Checkout
        uses: actions/checkout@v2
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      -
        name: Login to DockerHub
        uses: docker/login-action@v1 
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v2
        with:
          context: .
          file: ./Dockerfile
          platforms: linux/amd64
          push: true
          tags: {{ YOUR_DOCKERHUB_REPOSITORY }}/python-helloworld:latest
              
              
              
              
              ## API endpoint used to create the Application resource
apiVersion: argoproj.io/v1alpha1
kind: Application
## Set the name of the resource and namespace where it should be deployed.
## In this case the Application resource name is set to  `python-helloworld `
## and it is deployed in the `argocd` namespace
metadata:
  name: python-helloworld 
  namespace: argocd
spec:
  ## Set the target cluster and namespace to deploy the Python hello-world application.
  ## For example, the Python hello-world application is deployed in the `default` namespace
  ## within the local cluster or `https://kubernetes.default.svc`
  destination:
    namespace: default
    server: https://kubernetes.default.svc
  ## Set the project the application belongs to.
  ## In this case the `default` project is used.
  project: default
  ## Define the source of the Python hello-world application manifests.
  ## In this example, the manifests are stored in the `argocd-demo` repository
  ## under the `python-manifests` folder. Additionally, the latest commit within
  ## the repository is targeted or `HEAD`.
  source:
    path: python-manifests
    repoURL:
    https://github.com/kgamanji/argocd-demo
    targetRevision: HEAD
  # # Set the sync policy. 
  ## If left empty, the sync policy will default to manual.
  syncPolicy: {}
