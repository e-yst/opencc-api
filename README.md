# opencc-api

OpenCC integration with FastAPI. Includes a web UI powered by Quasar.

## Tech/Framework

Built with:

- [FastAPI](https://github.com/tiangolo/fastapi)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- [Quasar](https://github.com/quasarframework/quasar) - Frontend

## Installation

1. Clone this repository and its frontend submodule:

    ```sh
    git clone --recursive https://github.com/e-yst/opencc-api.git
    ```

### Frontend

1. Install Quasar CLI and build the frontend:

    ```sh
    cd opencc-quasar/
    yarn global add @quasar/cli
    yarn
    quasar build
    ```

2. Copy the built frontend static files to the backend:

    ```sh
    cp -r opencc-quasar/dist/spa/* opencc-api/opencc_api/static/
    ```

### Backend

1. Install OpenCC dependencies (for Ubuntu/Debian):

    ```sh
    apt-get update && apt-get install -y opencc
    ```

2. Install Python dependencies from `requirements/base.txt`:

    ```sh
    pip install -r requirements/base.txt
    ```

3. Run the backend server and access the API at `http://localhost:8000`:

    ```sh
    uvicorn app.main:app --host=0.0.0.0
    ```

## Docker

### Use existing image

1. Pull and run the image:

    ```sh
    docker run --rm -p 8000:8000 etys/opencc-api
    ```

### Build your own image

1. Build the Docker image:

    ```sh
    docker build -t opencc-api .
    ```

2. Run the image:

    ```sh
    docker run --rm -p 8000:8000 opencc-api
    ```

## License

MIT © [Eason Tse](https://github.com/e-yst)
