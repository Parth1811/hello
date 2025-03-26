
move_and_zoom() {
    local M=3
    local N=4
    local grid_index=$(( $1 - 1 ))

    local window_x=$(yabai -m query --windows --window | jq '.frame.x' | printf "%.0f")
    local window_y=$(yabai -m query --windows --window | jq '.frame.y' | printf "%.0f")
    local window_width=$(yabai -m query --windows --window | jq '.frame.w' | printf "%.0f")
    local window_height=$(yabai -m query --windows --window | jq '.frame.h' | printf "%.0f")

    echo "window_x: $window_x, window_y: $window_y, window_width: $window_width, window_height: $window_height"
    
    local grid_width=$(( window_width / N ))
    local grid_height=$(( window_height / M ))

    
    local row=$(( grid_index / N ))
    local col=$(( grid_index % N ))

    
    local center_x=$(( window_x + ((col * grid_width) + (grid_width / 2)) ))
    local center_y=$(( window_y + ((row * grid_height)) + (grid_height / 2) ))

    center_x=$(printf "%.0f" $center_x)
    center_y=$(printf "%.0f" $center_y)

    # echo "center_x: $center_x, center_y: $center_y, x: $window_x, y: $window_y, w: $window_width, h: $window_height"

    # echo "m:$center_x,$center_y"
    cliclick m:$center_x,$center_y
    osascript -e "tell application \"System Events\" to key code 53 using {option down}"
}

move_and_zoom ${@}
