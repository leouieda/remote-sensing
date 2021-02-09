.PHONY: serve

serve:
	xdg-open http://localhost:8000
	livereload -p 8000 lectures
