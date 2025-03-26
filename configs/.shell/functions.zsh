function search-pods(){
    eval $aliases[$1] get pods ${@:3} | grep $2
}

function vahan-orch-logs(){
    clear && printf '\e[3J'
    eval $aliases[$1] logs -f deployment/vahan-orchestrator-service | less +F
}

function warehouse-logs(){
    clear && printf '\e[3J'
    eval $aliases[$1] logs -f deployment/warehouse-service --container warehouse-service | less +F
}

function hardware-web-nginx-logs(){
    clear && printf '\e[3J'
    eval $aliases[$1] logs -f --container nginx deployment/hardware-web | less +F
}

function see-logs(){
    clear && printf '\e[3J'
    eval $aliases[$1] logs -f ${@:2} | less +F
}

function workon(){
    source ~/.virtualenv/$1/bin/activate
}


function openDesignatedApp(){
    myArray=("iTerm" "Visual Studio Code" "Adobe Acrobat Reader" "Postman" "Google Chrome" "Notion" "Slack" "WhatsApp" "Messages");
    space=$(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index)));
    open -a "${myArray[$space]}"
}

function openOrBringAppToThisSpace(){
    id=`yabai -m query --windows | jq "map(select(.app == \"$1\")) | .[0] | .id // empty"`
    if [ -z "$id" ]
    then
        open -a $1
    else
        yabai -m window $id --space $(($(/opt/homebrew/bin/yabai -m query --spaces --space | /opt/homebrew/bin/jq .index)))
        yabai -m window --focus $id
    fi
}
