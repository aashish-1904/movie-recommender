mkdir -p ~/.streamlit/

echo "\
[server]in\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml