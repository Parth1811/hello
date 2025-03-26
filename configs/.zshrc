export PATH="~/Library/Python/3.8/bin:$PATH"
export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"

source ~/powerlevel10k/powerlevel10k.zsh-theme
POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true
source ~/.p10k.zsh

source ~/.zsh_plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

export FZF_BASE="/usr/local/opt/fzf/install"
source ~/.zsh_plugins/zsh-interactive-cd.plugin.zsh
source ~/.zsh_plugins/fzf.plugin.zsh

source ~/.zsh_plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
DISABLE_MAGIC_FUNCTIONS="true"

# source ~/.zsh_plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh
source ~/.zsh_plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh
source ~/.zsh_plugins/wakatime-zsh-plugin/wakatime.plugin.zsh
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
source ~/.zsh_plugins/zsh-history-substring-search/zsh-history-substring-search.plugin.zsh

source ~/.shell/aliases
source ~/.shell/functions.zsh
source ~/.shell/env

autoload -U compinit && compinit
zmodload -i zsh/complist
# source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
# source /opt/homebrew/opt/chruby/share/chruby/auto.sh

# Load Angular CLI autocompletion.
# source <(ng completion script)

fpath+=~/.zfunc; autoload -Uz compinit; compinit

zstyle ':completion:*' menu select
