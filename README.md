# Proximity Tile Rendering Framework
 A basic module used to render tiles within a 1 tile radius of the player.

### Use case example: 
- Invisible maze.
- Can also be used as flashlight framework just tie player position to mouse position.

## Notes
- Can be scaled, you can scale window in the file under the window class in the dimensions variable, just make sure to add tiles to the tile_map in the tile class depending on the screen dimensions divided by 100.
- You can make tiles smaller, just make sure player movement speed and size are scaled down as well and once again add values to the tile_map.
- x-values in the tile_map are tied to the x value of the window dimensions.
- y-values in the tile_map are tied to the y value of the window dimensions.
- player.column = x
- player.row = y