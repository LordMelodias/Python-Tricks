from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": 'C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe'})

def overlay_text_on_video(video_path, text, output_path, position, font_size=50, start_time=0, end_time=None):
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    
    # Create a TextClip with the desired text
    text_clip = TextClip(text, fontsize=font_size, color='red', font="Arial-Bold")
    text_clip = text_clip.set_duration(video_clip.duration)
    
    # # Set the duration of the text (it will be displayed for the entire video by default)
    # if end_time:
    #     text_clip = text_clip.set_duration(end_time - start_time).set_start(start_time)
    # else:
    #     text_clip = text_clip.set_duration(video_clip.duration).set_start(start_time)
    
    # Set the position of the text
    text_clip = text_clip.set_position(position).set_fps(video_clip.fps)

    # Overlay the text on the video
    final_clip = CompositeVideoClip([video_clip, text_clip])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264")

# Example usage
overlay_text_on_video("video.mp4", "Hello, World!", "output_video_with_text.mp4", position=(638, 937), font_size=50, start_time=2, end_time=10)
