mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"akumar7_be20@thapar.edu\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
