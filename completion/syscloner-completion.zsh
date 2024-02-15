#compdef syscloner 

_syscloner() {
    local -a commands=("backup" "restore")

    _arguments \
        '1: :->command' \
        && return

    case $state in
        command)
            _describe 'command' commands
            ;;
    esac
}

_syscloner "$@"
