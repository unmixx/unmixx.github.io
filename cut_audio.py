from pydub import AudioSegment

def cut_segment(input_path, output_path, start_sec, end_sec):
    audio = AudioSegment.from_file(input_path)
    segment = audio[start_sec*1000 : end_sec*1000]  # 밀리초 단위
    segment.export(output_path, format="wav")

# 사용 예시: 2분 54초(174초) → 3분(180초)
cut_segment("1_＂Free＂ ｜ Official Lyric Video ｜ Sony Animation_(Vocals).wav", "free_cut.wav", 174, 181)
