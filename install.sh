#!/bin/bash

exe="syscloner"


if [ "$1" == "clean" ]; then
    # TODO uninstall
    echo "[INFO] Application uninstalled successfully"
    exit 0
fi

if [ -f "$exe" ]; then
    # Install the executable
    sudo cp ./$exe /usr/bin/$exe
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to copy the executable to /usr/bin/"
        exit 1
    fi
    echo "[INFO] $exe installed successfully"

    # Install Bash completion
    sudo install -g 0 -o 0 -m 0644 ./completion/$exe-completion.bash /etc/bash_completion.d/cchat
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to install Bash completion"
        exit 1
    fi
    echo "[INFO] bash completion installed successfully"

    # Install Zsh completion
    sudo install -m 644 ./completion/$exe-completion.zsh /usr/share/zsh/functions/Completion/_cchat
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to install Zsh completion"
        exit 1
    fi
    echo "[INFO] zsh completion installed successfully"

    # Install man page
    sudo install -g 0 -o 0 -m 0644 $exe.man /usr/share/man/man8/$exe.8
    sudo gzip /usr/share/man/man8/$exe.8
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to install man page"
        exit 1
    fi
    echo "[INFO] man page installed successfully"

    echo "[INFO] Installation completed successfully."
else
    echo "$exe is not built. Building..."
    # TODO build executable

    if [[ $? == 0 ]]; then
        ./install.sh
    else
        echo "Failed to build $exe"
        exit 1
    fi
fi

exit 0
