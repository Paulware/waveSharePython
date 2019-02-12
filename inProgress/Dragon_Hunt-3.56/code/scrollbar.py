#file: scrollbar.py
#Copyright (C) 2005 Evil Mr Henry and Phil Bordelon
#This file is part of Dragon Hunt.

#Dragon Hunt is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#Dragon Hunt is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with Dragon Hunt; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#This file contains scrollbar code.

import pygame
import g

class scrollbar:
	def __init__(self, xy, size, viewable_items, bg_color,
					fore_color, out_color):
		self.xy = xy
		self.size = (18, size)
		self.viewable_items = viewable_items
		self.space_for_each = size / viewable_items
		self.bg_color = bg_color
		self.out_color = out_color
		self.fore_color = fore_color

		self.scroll_area = size - 18*2

		self.scroll_surface = pygame.Surface(self.size)

		#create outline
		self.scroll_surface.fill(out_color)

		#create arrow bgs
		self.scroll_surface.fill(fore_color, (1, 1, self.size[0]-2, self.size[0]-2))

		self.scroll_surface.fill(fore_color, (1, self.size[1]-17, self.size[0]-2, self.size[0]-2))

		#create inner
		self.scroll_surface.fill(bg_color, (1, self.size[0], self.size[0]-2, self.size[1]-36))



		#create arrows
		self.scroll_surface.blit(g.buttons["arrow.png"], (1, 1))
		self.scroll_surface.blit(pygame.transform.flip(
								g.buttons["arrow.png"], 0, 1), (1, self.size[1]-17))

		self.refresh_scroll(0, 100)
	def refresh_scroll(self, start_item, total_items):
		if start_item > total_items - self.viewable_items:
			start_item = total_items - self.viewable_items

		g.screen.blit(self.scroll_surface, self.xy)

		#middle gripper
		self.start_y = self.size[0] + (self.scroll_area * start_item) / total_items
		self.size_y = (self.scroll_area * self.viewable_items) / total_items

		g.screen.fill(self.fore_color, (self.xy[0]+1, self.xy[1]+self.start_y,
						self.size[0]-2, self.size_y))
	def is_over(self, xy):
		if xy[0] >= self.xy[0] and xy[1] >= self.xy[1] and \
					xy[0] <= self.xy[0] + self.size[0] \
					and xy[1] <= self.xy[1] + self.size[1]:
			if xy[1] <= self.xy[1] + self.size[0]: #up arrow
				return 1
			elif xy[1] >= self.xy[1] + self.size[1] - self.size[0]: #dn arrow
				return 2
			elif xy[1] <= self.xy[1]+self.start_y: #upper gutter
				return 3
			elif xy[1] >= self.xy[1]+self.start_y + self.size_y: #lower gutterx
				return 4
			#If I want the gripper working, code here.
		return -1
	def adjust_pos(self, event, list_pos, item_list):
		if event.type != pygame.MOUSEBUTTONUP: return list_pos
		if event.button != 1: return list_pos
		xy = event.pos
		tmp = self.is_over(xy)
		if tmp == 1:
			list_pos -= 1
			if list_pos < 0:
				list_pos = 0
		elif tmp == 2:
			list_pos += 1
			if list_pos >= len(item_list):
				list_pos = len(item_list) - 1
		elif tmp == 3:
			list_pos -= self.viewable_items
			if list_pos < 0:
				list_pos = 0
		elif tmp == 4:
			list_pos += self.viewable_items
			if list_pos >= len(item_list) - 1:
				list_pos = len(item_list) - 1
		return list_pos



