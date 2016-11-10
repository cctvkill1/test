while true

do
	for i in {1..14}
	do  
		ps aux | grep getBitData$i.py | grep -v grep
		if [ $? -eq 0 ];then
			#找到了
			echo ok
		else
			echo error
			#没找到，启动
			python getBitData$i.py &
		fi  
	done
	
	ps aux | grep index.py | grep -v grep
	if [ $? -eq 0 ];then
		#找到了
		echo ok
	else
		echo error
		#没找到，启动
		python /opt/bit-web/index.py &
	fi  
	
	sleep 10
done