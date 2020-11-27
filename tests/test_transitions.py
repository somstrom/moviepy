import os

import pytest

from moviepy.video.compositing.transitions import slide_out
from moviepy.video.compositing.transitions import slide_in
from moviepy.video.VideoClip import BitmapClip, ColorClip
from moviepy.video.compositing.transitions import crossfadeout
from moviepy.video.compositing.transitions import crossfadein


def test_crossfadein():
    clip = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    clip1 = crossfadein(clip, duration=3)
    target1 = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    assert clip1 == target1

    clip = BitmapClip([["AAA"], ["AAA"], ["AAA"]], fps=1)
    clip2 = crossfadein(clip, duration=1)
    target2 = BitmapClip([["AAA"], ["AAA"], ["AAA"]], fps=1)
    assert clip2 == target2


def test_crossfadeout():
    clip = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    clip1 = crossfadeout(clip, duration=3)
    target1 = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    assert clip1 == target1


def test_slide_in():
    clip = BitmapClip([[["A"], ["B"], ["C"]], [["A"], ["B"], ["C"]]], fps=1)
    clip1 = slide_in(clip, duration=3, side="bottom")
    target1 = BitmapClip([[["A"], ["B"], ["C"]], [["A"], ["B"], ["C"]]], fps=1)
    assert clip1 == target1


def test_slide_out():
    clip = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    clip1 = slide_out(clip, duration=1, side="left")
    target1 = BitmapClip([["ABC"], ["ABC"], ["ABC"]], fps=1)
    assert clip1 == target1



if __name__ == "__main__":
    pytest.main()
