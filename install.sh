#!/bin/bash

exe="syscloner"


if [ "$1" == "clean" ]; then
    sudo rm /usr/bin/$exe
    sudo rm /etc/bash_completion.d/$exe
    sudo rm /usr/share/zsh/functions/Completion/_$exe 
    sudo rm /usr/share/man/man8/$exe.8.gz
    rm -r build
    rm -r dist
    rm *.spec

    echo "[INFO] Application uninstalled successfully"
    exit 0
fi

if [ -f "./dist/main" ]; then
    # Install the executable
    sudo cp ./dist/main /usr/bin/$exe
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to copy the executable to /usr/bin/"
        exit 1
    fi
    echo "[INFO] $exe installed successfully"

    # Install Bash completion
    sudo install -g 0 -o 0 -m 0644 ./completion/$exe-completion.bash /etc/bash_completion.d/$exe
    if [ $? -ne 0 ]; then
        echo "[ERRO] Failed to install Bash completion"
        exit 1
    fi
    echo "[INFO] bash completion installed successfully"

    # Install Zsh completion
    sudo install -m 644 ./completion/$exe-completion.zsh /usr/share/zsh/functions/Completion/_$exe
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
    echo "[WARN] $exe is not built. Building..."
    
    # Install pip if not already installed
    if ! command -v pip > /dev/null 2>&1; then
        echo "[WARN] pip is not installed"
        echo "[INFO] Installing..."
        wget https://bootstrap.pypa.io/get-pip.py
        python3 get-pip.py

        if [ $? -ne 0 ]; then
            echo "[ERRO] Could not install pip. Please install manually before running the script again"
            exit 1
        else
            rm get-pip.py
            echo "[INFO] pip installed successfully"
        fi
    fi

    pip install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "[ERRO] Could not install pyinstaller using pip. Plese try installing pyinstaller using your package manager before running the script again"
        exit 1
    fi

    pyinstaller --onefile src/main.py

    if [[ $? == 0 ]]; then
        ./install.sh
    else
        echo "[ERRO] Failed to build $exe"
        exit 1
    fi
fi

exit 0
