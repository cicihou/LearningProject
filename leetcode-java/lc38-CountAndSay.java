class Solution {
	public String countAndSay(int n) {
		String ans = alg(n);
		return ans ;
	}

	public String countAndSay(String n) {
		String ans = alg(n);
		return ans ;
	}

	private String alg(String s) {
		String cur = "";
		int m = s.length();
		for (int j = 0; j < m; ){
			int k = j + 1;
			while (k < m && s.charAt(j) == s.charAt(k)) k++;
			int cnt = k-j;
			cur += cnt + "" + s.charAt(j);
			j = k;
		}
		return cur;
	}

	private String alg(int n) {
		String ans = "1";
		for (int i = 2; i <= n; i++){
			String cur = alg(ans);
			ans = cur;
		}
		return ans;
	}
}
