    typeset -A desktophash
    desktophash[0]=29
    desktophash[1]=18
    desktophash[2]=19
    desktophash[3]=20
    desktophash[4]=21
    desktophash[5]=23
    desktophash[6]=22
    desktophash[7]=26
    desktophash[8]=28
    desktophash[9]=25
    desktophash[10]=29
    desktophash[11]=27
    desktophash[12]=24
    desktopkey=${desktophash[$1]}
    osascript -e "tell application \"System Events\" to key code $desktopkey using {control down, command down, shift down, option down}"
}

function switchSpace(){
    case "$1" in
            left)
                space=`v=$(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index))); echo $(( (v - 1) % 4 < 1 ? v : v - 1))`
                ;;

            right)
                space=`v=$(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index))); echo $(( (v - 1) % 4 > 2 ? v : v + 1))`
                ;;

            up)
                 space=`v=$(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index) - 4)); echo $((v < 0 ? v + 4 : v))`
                ;;
            down)
                space=`v=$(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index) + 4)); echo $((v > 12 ? v - 4 : v))`
                ;;
            *)
                echo $"Usage: $0 {left|right|up|down}"
                return 1
    esac

    if [[ $# -eq 2 ]];
    then
        yabai -m window --space $space && yabai -m space --focus $space

    else
        yabai -m space --focus $space
    fi


}

# Pass input arguments to switchSpace function
switchSpace ${@}
