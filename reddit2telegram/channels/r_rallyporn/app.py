#encoding:utf-8

subreddit = 'rallyporn'
t_channel = '@r_rallyporn'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
