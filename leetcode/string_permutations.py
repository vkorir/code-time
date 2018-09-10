"""
victor => v i c t o r vi ic ct to or vic ict cto tor vict icto ctor victo ictor victor
"""


def permute(s):
	if len(s) == 2:
		yield s
		yield s[1:] + s[:1]
	else:
		for i in range(len(s)):
			for perm in permute(s[:i] + s[i+1:]):
				yield s[i] + perm