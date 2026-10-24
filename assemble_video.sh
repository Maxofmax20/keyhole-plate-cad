#!/usr/bin/env bash
set -euo pipefail
cd /data/keyhole-plate-blender
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
VF="minterpolate=fps=24:mi_mode=mci:mc_mode=obmc:me_mode=bidir"
VF="$VF,drawbox=x=0:y=0:w=iw:h=73:color=0x071421@0.87:t=fill"
VF="$VF,drawtext=fontfile=$FONT:text='KEYHOLE QUICK RELEASE  -  CAD CONCEPT V1':fontcolor=white:fontsize=24:x=26:y=22"
VF="$VF,drawbox=x=0:y=466:w=iw:h=74:color=0x071421@0.90:t=fill"
VF="$VF,drawtext=fontfile=$FONT:text='44x44 mm plate  |  19.6 mm entry  |  17.8 mm head  |  15 mm travel':fontcolor=0xa3c8e8:fontsize=19:x=27:y=507"
VF="$VF,drawtext=fontfile=$FONT:text='01    THE TWO PARTS':fontcolor=white:fontsize=23:x=26:y=477:enable='between(t,0,1.15)'"
VF="$VF,drawtext=fontfile=$FONT:text='02    ALIGN CIRCULAR ENTRY':fontcolor=white:fontsize=23:x=26:y=477:enable='between(t,1.15,2.2)'"
VF="$VF,drawtext=fontfile=$FONT:text='03    INSERT BUTTON':fontcolor=white:fontsize=23:x=26:y=477:enable='between(t,2.2,3.05)'"
VF="$VF,drawtext=fontfile=$FONT:text='04    SLIDE PLATE DOWN TO LOCK':fontcolor=white:fontsize=23:x=26:y=477:enable='between(t,3.05,4.35)'"
VF="$VF,drawtext=fontfile=$FONT:text='05    LOCKED ASSEMBLY':fontcolor=white:fontsize=23:x=26:y=477:enable='between(t,4.35,6)'"
ffmpeg -y -hide_banner -loglevel error -stats -framerate 8 -i frames/frame_%04d.png -vf "$VF" -c:v libx264 -crf 19 -preset veryfast -pix_fmt yuv420p -movflags +faststart keyhole_assembly.mp4
ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,nb_frames,avg_frame_rate -of default=noprint_wrappers=1 keyhole_assembly.mp4
