require 'set'

reds = File.readlines("input.txt", chomp: true).map { |l|
  x, y = l.split(",").map(&:to_i)
  [x, y]
}

redset = reds.to_set
greens = Set.new

(0...reds.size).each do |i|
  x1, y1 = reds[i]
  x2, y2 = reds[(i+1) % reds.size]

  if x1 == x2
    Range.new(*[y1,y2].minmax).each { |y| greens << [x1, y] }
  else
    Range.new(*[x1,x2].minmax).each { |x| greens << [x, y1] }
  end
end

minx, maxx = reds.map(&:first).minmax
miny, maxy = reds.map(&:last).minmax

def inside?(px, py, poly)
  c = false
  j = poly.length - 1
  poly.each_with_index do |(xi, yi), i|
    xj, yj = poly[j]
    if ((yi > py) != (yj > py)) &&
        px < (xj - xi) * (py - yi) / (yj - yi).to_f + xi
      c = !c
    end
    j = i
  end
  c
end
puts maxx
(minx..maxx).each do |x|
  puts x
  (miny..maxy).each do |y|
    next if redset.include?([x,y]) || greens.include?([x,y])
    greens << [x,y] if inside?(x+0.5, y+0.5, reds)
  end
end
puts "b" 
allowed = redset | greens

best = 0

reds.combination(2).each do |a, b|
  lx, rx = [a[0], b[0]].minmax
  ty, by = [a[1], b[1]].minmax

  area = (rx-lx+1) * (by-ty+1)
  next if area <= best

  ok = true
  (lx..rx).each do |x|
    (ty..by).each do |y|
      unless allowed.include?([x,y])
        ok = false
        break
      end
    end
    break unless ok
  end

  best = area if ok
  puts best if ok
end

puts best
