# 4033. Valid K-Unique Subarrays I

**Difficulty:** Hard  
[View on LeetCode](https://leetcode.com/problems/valid-k-unique-subarrays-i/)

---

You are given an integer array `nums` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]` represents the **subarray** `nums[l_i..r_i]`.

For each query, the **subarray** `nums[l_i..r_i]` is considered **valid** if:

- It contains **exactly** `k` **distinct** numbers, and
- The **frequency** of every number in the **subarray** is **even**.

Return a boolean array `ans`, where `ans[i]` is `true` if `nums[l_i..r_i]` is **valid**, and `false` otherwise.

**Example 1:**

**Input:** nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]

**Output:** [false,true,false]

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>[l<sub>i</sub>, r<sub>i</sub>]</code></th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Unique numbers</th>
			<th style="border: 1px solid black;">Frequency</th>
			<th style="border: 1px solid black;">Validity check</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[0, 1]</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">{1, 2} &rarr; 2</td>
			<td style="border: 1px solid black;">{1: 1, 2: 1}</td>
			<td style="border: 1px solid black;"><code>false</code>: Element counts are not even.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 3]</td>
			<td style="border: 1px solid black;">[1, 2, 2, 1]</td>
			<td style="border: 1px solid black;">{1, 2} &rarr; 2</td>
			<td style="border: 1px solid black;">{1: 2, 2: 2}</td>
			<td style="border: 1px solid black;"><code>true</code>: Exactly <code>k = 2</code> distinct elements, all appear&nbsp;an even number of times.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[2, 2]</td>
			<td style="border: 1px solid black;">{2} &rarr; 1</td>
			<td style="border: 1px solid black;">{2: 2}</td>
			<td style="border: 1px solid black;"><code>false</code>: Number of distinct elements is less than <code>k = 2</code>.</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [false, true, false]`.

**Example 2:**

**Input:** nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]

**Output:** [true,false]

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>[l<sub>i</sub>, r<sub>i</sub>]</code></th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Unique numbers</th>
			<th style="border: 1px solid black;">Frequency</th>
			<th style="border: 1px solid black;">Validity check</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">[1, 2]</td>
			<td style="border: 1px solid black;">[3, 3]</td>
			<td style="border: 1px solid black;">{3} &rarr; 1</td>
			<td style="border: 1px solid black;">{3: 2}</td>
			<td style="border: 1px solid black;"><code>true</code>: Exactly <code>k = 1</code> distinct element, appears an&nbsp;even number of times.</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0, 2]</td>
			<td style="border: 1px solid black;">[3, 3, 3]</td>
			<td style="border: 1px solid black;">{3} &rarr; 1</td>
			<td style="border: 1px solid black;">{3: 3}</td>
			<td style="border: 1px solid black;"><code>false</code>: 3 does not appear an even number of times.</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [true, false]`.

**Constraints:**

- `2 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= n`
- `1 <= queries.length <= 10^5`
- `queries[i] == [l_i, r_i]`
- `0 <= l_i < r_i <= n - 1`
