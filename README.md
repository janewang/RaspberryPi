Raspberry Pi
============

Tinkering..

![raspberrypi jpeg](https://github.com/janewang/RaspberryPi/blob/master/raspberrypi.jpeg)

## Setup Instruction

#### SD Card Image
I chose Arch Linux ARM because QtonPi is dead and the other images do not give you as much control. On Mac OS X the following instruction should get you set up with the SD Card Image.

- Download Arch Linux ARM using BitTorrent.
- Checksum `sha1sum ~/archlinuxarm-13-06-2012.zip`
- `cd Volumes` `ls` Locate the SD Card.
- `df -h` and copy its name. Mine was /dev/disk3s1
- `sudo diskutil unmount /dev/disk3s1`
- `sudo dd bs=1m if=~/Downloads/archlinuxarm-13-06-2012/archlinuxarm-13-06-2012.img of=/dev/rdisk3`
- Wait patiently until the write to SD card is completed.

#### Plug Everything into the Raspberry Pi
You will need a lot of pieces - collect them all from your spare parts box (charger, mouse), your computer (monitor, keyboard, mouse), your mobile phone (charger), your camera (SD card - formatted as above), and your TV (monitor).

When you plug in the power, a red light should turn on. The rest of shinny bright lights should all turn on. Check your screen and see if there is a Raspberry. Wait for it...

It will promote for login.
- Username: root
- Password: root

#### Download LXDE (A Desktop Environment)
- Update packages `pacman -Syn`
- Install LXDE `pacman -S lxde xorg-xinit xf86-video-fbdev`
- To run a LXDE session `xinit /usr/bin/lxsession`

Congratulations, you can download more programs and optimize it to your liking. It's just like what you'd do on the Mac. Enjoy!