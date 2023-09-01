# Server for Text Vectorization

This is a Python server that uses the Hugging Face Transformers library to convert text into embeddings and returns the embeddings as JSON. Additionally, it supports quantization of embeddings.

## Getting Started

These instructions will help you set up and run the server on your local machine.

### Prerequisites

- Python 3.9 (or a compatible version)
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

```bash
   git clone https://github.com/onepeerlabs/huggingface-embeddings.git
   cd your-server
```

2. Install the required Python packages:

```bash
   pip install -r requirements.txt
```

### Running the Server

To run the server locally, execute the following command:

```bash
    python app.py --model-name sentence-transformers/all-MiniLM-L6-v2
```

By default, the server will listen on port 9876. You can customize the port by modifying the code in `app.py`.

### Running with Docker

You can also run the server in a Docker container. First, build the Docker image:

```bash
    docker build -t onepeerlabs/huggingface-embeddings .
```

Run the container:

```bash
    docker run -p 9876:9876 onepeerlabs/huggingface-embeddings --model-name sentence-transformers/all-MiniLM-L6-v2
```

### API Endpoints

- `/health`: A health check endpoint that returns "OK" when the server is running.

- `/vectorize`: Accepts a JSON request with a "query" field containing the text to vectorize. Returns the embeddings as a JSON response.

## Usage

You can send POST requests to the `/vectorize` endpoint to obtain embeddings for text. For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": ["your text here"]}' http://localhost:9876/vectorize
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your fork on GitHub.
5. Create a pull request to the main repository.

## License

TODO