---
comments: true
layout: tutorial
assets-dir: assets/blog/eagle_beginner
permalink: /blog/eagle_beginner/
categories: blog
topic_folder: eagle_beginner
title: Eagle Tutorial for absolute beginners.
tags: [Eagle, beginners, Tutorial]
last_updated: 2018-07-27
excerpt: Eagle is a computer-aided circuit-designing,PCB designing and a circuit simulation software developed by Autodesk.
contributors: Sakshee Pimpale
---

**Eagle** is a computer-aided circuit-designing,PCB designing and a circuit simulation software developed by **Autodesk**.I hope you will enjoy working with this light,easy-to-use and download yet useful application.


<h1>TABLE OF CONTENTS</h1>

* TOC
{:toc}
<hr>

## HOW TO DOWNLOAD EAGLE?

You can download the software from <u><a href="https://www.autodesk.com/products/eagle/free-download">here.</a></u>
The latest version is just 115Mb and installer gets downloaded in minutes.
Run the installer and it gets downloaded quite easily.




## MAKING A NEW PROJECT

Open Eagle.
Then in control panel(which opens)->File->New->Project.Name the project
Open up a new schematic using File->New->Schematic and then save it in the project directory using File->save as in schematic window with .sch extension.

### Working with the schematic:

#### Step 1:
- <big>Adding components </big>:

  There are inbuilt libraries in eagle from which components can directly be copied.Edit->ADD or directly click on ADD symbol in the toolbar to the left.To search for any keyword in the standard libraries :search  enter *keyword*.The * acts as a wildcard entry,it is absolutely necessary if we don’t have the exact name. Eg. if we want IC 555 timer we may search *555* and then get the required LM555 ic.

![Adding a component]({{ site.url }}/{{ page.assets-dir }}/1.jpg)
<small>
-- Click “ok”
-- Then right click to rotate.
-- Position by moving the mouse.
-- Left click to place.
</small>

- <big>Adding more libraries to the ADD feature:
Visit <u><a href="https://www.diymodules.org/eagle-libraries ">this website</a></u> for libraries for libraries</big>

  <small>Follow the  instructions from the given <u><a href="http://www.instructables.com/id/Adding-a-Library-to-Eagle-CAD/">link</a></u> to USE it:
  This will make the library elements appear as we use the ADD option.
  </small>

#### Step 2:

- Make the connections using Draw->Net
- Use a net instead of wire for electrical connections.
(Nets will automatically form junctions when terminated on pins or other nets. Wire don’t make termination dots and wont auto-terminate the connection.)

## IMPORTANT COMMANDS NEEDED:DELETE,MOVE,ROTATE,GROUP

In the toolbox to the left you will find all important commands.

- <b><big>DELETE:</big></b>
  1. Click on delete tool in the toolbox to the left.
  2. For every object in eagle(except for nets and buses) you will find a plus sign(crosshair).
  3. Hover to the crosshair,left click and the object gets deleted.

- <b><big>MOVE:</big></b>
  1. Click on move tool in the toolbox to the left.
  2. For every object in eagle(except for nets and buses) you will find a plus sign(crosshair).
  3. Hover to the crosshair,left click ,move to desired location,left click again to place.

- <b><big>ROTATE:</big></b>
  1. Hovering over the crosswire with rotate tool selected and left clicking rotates the object.

- <b><big>GROUP:</big></b>
  1. Use the group tool.
  2. Draw polygon covering group elements.Right click to complete it.
  3. Use the command delete or move or rotate  +ctrl+right click to perform the action on the group.

- <b><big>ERC (Electrical Rule Check)</big></b>
  1. This command in toolbox, helps to check electrical errors.

<center>There are many more useful tools in the toolbox.</center>
![Commands under Edit option]({{ site.url }}/{{ page.assets-dir }}/2.jpg)


## SPECIAL COMMANDS FOR SCHEMATICS

| TEXT        | Insert Text       |
|  Junction   | Place connection point      |           
| INVOKE      | Add certain 'gate' from a placed device       |
| LABEL       | Provide label to bus or net       |
| GATESWAP    | Swap equivalent 'gates'       |
| PINSWAP     | Swap equivalent pins       |
| BOARD       | Create a board from a schematic       |

Click on them. <br/>
Directions to use each are provided in eagle at the bottom.
![Commands under draw option]({{ site.url }}/{{ page.assets-dir }}/3.jpg)



## EXPORTING THE FILE

- <big><b>As pdf</b></big>
( in schematic window)
  1. Chose Print to file(PDF) in Printer.
  2. Chose the location of output PDF file in Output file option.
  3. Click OK and we’re done.
  ![export as pdf]({{ site.url }}/{{ page.assets-dir }}/4.jpg)


- <big><b>As Image</b></big>
  1. File->Export->Image
  2. In the dialog box that appears,
  3. Chose the location and name of the imagederised and click Ok.
  ![export as image]({{ site.url }}/{{ page.assets-dir }}/5.jpg)


**_Time to make some good circuit design using eagle. Happy tinkering!_**
