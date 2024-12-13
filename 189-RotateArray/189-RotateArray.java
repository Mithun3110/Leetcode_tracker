var last = 0
var count = 0
var i = 0
var tmp = nums(i)

var start = 0
while (count < n) {
  last = (i + k) % n
  val tmp1 = nums(last)
  nums(last) = tmp
  tmp = tmp1
  i = last
  count += 1
  if (count < n && last == start) {
    start += 1
    i = start
    tmp = nums(i)
  }
}