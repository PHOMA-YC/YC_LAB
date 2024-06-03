def solution(id_list, report, k):
    # 각 유저별로 신고한 사람들을 저장할 딕셔너리
    report_dict = {user: set() for user in id_list}
    
    # 각 유저별로 신고당한 횟수를 저장할 딕셔너리
    report_count = {user: 0 for user in id_list}
    
    # report 리스트에서 중복 제거
    unique_reports = set(report)
    
    # 신고자와 신고 당한 사람을 분리하여 저장
    # 신고받은사람이 신고자 명단에 없으면 신고자에 받은사람 명단 추가후 횟수 1 증가
    
    for rep in unique_reports:
        reporter, reported = rep.split()
        if reported not in report_dict[reporter]:
            report_dict[reporter].add(reported)
            report_count[reported] += 1
    
    # k번 이상 신고 당한 사람에게 메일을 보낼 신고자 목록을 저장할 딕셔너리
    mail_dict = {user: 0 for user in id_list}
    
    # k번 이상 신고 당한 사람을 찾아 메일 수를 업데이트
    for reporter, reported_users in report_dict.items():
        for reported in reported_users:
            if report_count[reported] >= k:
                mail_dict[reporter] += 1
    
    # 결과 출력
    answer = [mail_dict[user] for user in id_list]
    return answer

