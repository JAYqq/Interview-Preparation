def main(step):
    # if step==0:
    #     return 0
    # if step==1:
    #     return 1
    # if step==2:
    #     return 2
    # dp=[0 for _ in range(step+1)]
    # dp[0]=0
    # dp[1]=1
    # dp[2]=2
    # for i in range(3,step+1):
    #     dp[i]=sum(dp[0:i])+1
    # return dp[step]
    if step<=0:return 0
    return pow(2,step-1)
print(main(1000))


# public class JavaTest {
# 	public static void main(String[] args) {
# 		Scanner input = new Scanner(System.in);
# 		int target = input.nextInt();
# 		System.out.println("跳上一个" + target + "级的台阶总共有"
# 				+ jumpFloor(target) + "种跳法");
# 	}
# 	// 第一种做法
# 	public static int jumpFloor(int target) {
# 		if (target <= 0) return 0;
# 		return (int) Math.pow(2, target - 1);
# 	}
# //       第二种做法
# //	public static int jumpFloor(int target) {
# //		if (target <= 0) return 0;
# //		if (target == 1) return 1;
# //		int a = 1;
# //		int b = 2;
# //		for (int i = 2; i <= target; i++) {
# //			b = 2 * a;
# //			a = b;
# //		}
# //		return b;
# //	}
# }