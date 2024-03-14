.PHONY: test clean

test: ## Ejecutar pruebas con pytest
	pytest

clean: ## Eliminar archivos de Python generados
	find . -type f -name '*.pyc' -exec rm {} +
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type d -name '.pytest_cache' -exec rm -r {} +


.PHONY: help

help: ## Mostrar esta ayuda.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "Uso: make <target>"
	@echo "Objetivos disponibles:"
	@echo
	@echo "Instalación y Pruebas:"
	@echo "  install     Instalar dependencias del proyecto"
	@echo "  test        Ejecutar pruebas con pytest"
	@echo "  clean       Eliminar archivos de Python generados"