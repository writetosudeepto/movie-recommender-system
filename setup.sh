mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection=false
" > ~/.streamlit/config.toml