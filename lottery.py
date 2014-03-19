import random
import time

ranked_teams = ()


ordinal = lambda n: '%d%s' % (n, 'tsnrhtdd'[(n/10%10 != 1) * (n% 10 < 4) * n % 10::4])

def seed_teams():
  teams = {}
  if not ranked_teams:
    # Prompt for rankings
    for iter in range(12):
      num_balls = iter + 1
      raw_input('Which team finished in %s place? ' % ordinal(num_balls))
      teams[iter] = num_balls
  else:
    i = 1
    for t in ranked_teams:
      print ('%s. %s' % (i, t))
      teams[t] = i
      i += 1
  return teams


def assign_balls(teams):
  balls = []
  for t, num_balls in teams.iteritems():
    start = len(balls)
    end = start + num_balls
    for ball in range(start, end):
      balls.append(t)
  print ('Lottery balls: ', balls)
  return balls


def draw_picks(teams, balls):
  order = []
  remaining_balls = balls
  for i in range(1, len(teams) + 1):
    print ('......................................')
    print ('Remaining balls: %s %s' % (len(remaining_balls), remaining_balls))
    pick = pull_ball(i, remaining_balls)
    order.append(pick)

    picked_team_num_balls = len(filter(lambda a: a == pick, remaining_balls))
    print ('Pick %s is: %s, with %s / %s balls' % (i, pick, picked_team_num_balls, len(remaining_balls)))
    print ('Removing %s\'s balls' % pick)
    remaining_balls = filter(lambda a: a != pick, remaining_balls)
    print ('......................................')
    raw_input('Proceed with the next pick?')

  print ('Picks are done. Final results:')
  for i, team in enumerate(order):
    print ('Pick %s: %s' % (i+1, team))

def pull_ball(num_pick, balls):
# Pulls random ball and removes all other balls of that team.
  lower_bound = 0
  upper_bound = len(balls) - 1
  print ('Drawing pick %s... ' % num_pick)
  pick_index = random.randint(lower_bound, upper_bound)
  print ('Selected: %s' % pick_index)
  pick = balls[pick_index]
  return pick

  


print ('RANKINGS..........')
teams = seed_teams()
print ('ASSIGNING. . . . .')
balls = assign_balls(teams)
print ('DRAWING...........')
draw_picks(teams, balls)
