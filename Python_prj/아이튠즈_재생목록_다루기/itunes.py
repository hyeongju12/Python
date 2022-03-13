# 중복곡 찾기
import plistlib


def findDuplicates(fileName):
    print(f'Finding duplicate tracks in {fileName}')

    # 파일에서 재생목록 로드 -> plist 변수에 저장
    plist = plistlib.load(fileName)

    # track을 얻는다
    tracks = plist['Tracks']

    # 트랙 이름의ㅏ 딕셔너리 생성
    tracksNames = {}

    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # 이미 존재하는 항목 처리
            if name in tracksNames:
                if duration//1000 == tracksNames[name][0]//1000:
                    count = tracksNames[name][1]
                    tracksNames[name] = (duration, count+1)
            else:
                tracksNames[name] = (duration, 1)
        except:
            pass
