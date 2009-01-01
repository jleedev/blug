from __future__ import with_statement
from django.shortcuts import *
import os,os.path,re,datetime

format = re.compile(r'(\d+)-(\d+)-(\d+)-([-_a-z0-9]+).text')

def list_entries():
	for filename in os.listdir('entries'):
		match = format.match(filename)
		if not match: continue
		(yyyy,mm,dd,slug) = match.groups()
		date = datetime.date(*map(int,(yyyy,mm,dd)))
		url = '%s/%s/%s/%s/' % (yyyy,mm,dd,slug)
		with open(os.path.join('entries',filename)) as f:
			title = f.readline().strip() or slug
		yield dict(title=title, date=date, url=url)

def index(request):
	listing = sorted(list_entries(), key=lambda entry: entry['date'], reverse=True)
	return render_to_response('blug/index.html', locals())

def entry(request, yyyy, mm, dd, slug):
	try:
		filename = '%s-%s-%s-%s.text' % (yyyy,mm,dd,slug)
		with open(os.path.join('entries',filename)) as f:
			content = f.read()
		return render_to_response('blug/entry.html', locals())
	except IOError:
		raise Http404
