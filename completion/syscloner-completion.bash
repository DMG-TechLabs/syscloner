_system_cloner_completion() {
    local cur prev words
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    words=("backup" "restore")

    case "${prev}" in
        syscloner)
            COMPREPLY=($(compgen -W "${words[*]}" -- "${cur}"))
            return 0
            ;;
    esac
}
complete -F _system_cloner_completion syscloner
