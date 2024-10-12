#!/bin/bash

# Mostra a pasta/diretório onde você está
echo "Diretório atual:"
pwd

# Gera uma lista com detalhes do conteúdo da pasta HOME e redireciona para lista_HOME.txt
ls -l ~ > lista_HOME.txt

# Imprime a data atual na tela
echo "Data atual:"
date
