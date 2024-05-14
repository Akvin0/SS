import requests
import winsound

def main():
	latest = 0
	
	while True:
		res = requests.get('https://freelance.habr.com/tasks?only_with_price=true').text
		for s in res.split('\n'):
			if (s.startswith('Заказы ')):
				orders = s.split('Заказы (')[1]
				orders = int(orders[0:len(orders)-1])
				if (latest != orders):
					if (orders > latest):
						latest = orders
						print(latest)
						winsound.Beep(440, 500) # Hz, duration
					else:
						latest = orders

if __name__ == '__main__':
	main()