
def main():
	f = open('input.txt', 'r')

	T = int(f.readline())
	
	for i in range(1, T + 1):
		nums = f.readline().strip().split(' ')
		N, K, V = int(nums[0]), int(nums[1]), int(nums[2])
		
		names = [f.readline().replace('\n', '') for _ in range(N)]
		index = 0
		for _ in range(0, V % N - 1):
			index = (index + K) % N
		print(index)
		inds = []
		while len(inds) < K:
			inds.append(index)
			index = (index + 1) % N
		inds.sort()
		res = [names[k] for k in inds]
		print('Case #' + str(i) + ': ' + ' '.join(res))

if __name__ == '__main__':
	main()