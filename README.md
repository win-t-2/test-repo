# Simple HTTP Server

A simple HTTP server that serves "hello world" text for all GET requests.

## Usage

Run the server with default settings (port 8000):

```bash
python3 server.py
```

Or specify a custom port:

```bash
python3 server.py 3000
```

The server will start and listen on `0.0.0.0` (all network interfaces) at the specified port.

## Testing

Once the server is running, you can test it with:

```bash
curl http://localhost:8000
```

Or open `http://localhost:8000` in your web browser.

## Requirements

- Python 3.x (uses built-in `http.server` module)
