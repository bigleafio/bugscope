# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class BugzillaMozillaOrgSpider(scrapy.Spider):
    name = 'bugzilla.mozilla.org'
    limit = 2

    def start_requests(self):
        urls = [
            # Firefox
            'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox&buglist.cgi?' +
            'bug_status=UNCONFIRMED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),

            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox&buglist.cgi?' +
            # 'bug_status=NEW&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&value0-0-3=%2A&' +
            # 'order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox&buglist.cgi? + '
            # 'bug_status=ASSIGNED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&'
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&'
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&'
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox&buglist.cgi?' +
            # 'bug_status=REOPEN&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # # Core
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Core&buglist.cgi?' +
            # 'bug_status=UNCONFIRMED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Core&buglist.cgi?' +
            # 'bug_status=NEW&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&value0-0-3=%2A&' +
            # 'order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Core&buglist.cgi? + '
            # 'bug_status=ASSIGNED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&'
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&'
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&'
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Core&buglist.cgi?' +
            # 'bug_status=REOPEN&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            # # Firefox iOS
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=product=Firefox%20for%20iOS&buglist.cgi?' +
            # 'bug_status=UNCONFIRMED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=product=Firefox%20for%20iOS&buglist.cgi?' +
            # 'bug_status=NEW&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&value0-0-3=%2A&' +
            # 'order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=product=Firefox%20for%20iOS&buglist.cgi? + '
            # 'bug_status=ASSIGNED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&'
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&'
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&'
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=product=Firefox%20for%20iOS&buglist.cgi?' +
            # 'bug_status=REOPEN&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # # Firefox Android
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox%20for%20Android&buglist.cgi?' +
            # 'bug_status=UNCONFIRMED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox%20for%20Android&buglist.cgi?' +
            # 'bug_status=NEW&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&value0-0-3=%2A&' +
            # 'order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox%20for%20Android&buglist.cgi? + '
            # 'bug_status=ASSIGNED&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&'
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&'
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&'
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit),
            #
            # 'https://bugzilla.mozilla.org/buglist.cgi?product=Firefox%20for%20Android&buglist.cgi?' +
            # 'bug_status=REOPEN&field0-0-0=alias&field0-0-1=short_desc&field0-0-2=status_whiteboard&' +
            # 'field0-0-3=cf_crash_signature&query_format=advanced&type0-0-0=substring&type0-0-1=substring&' +
            # 'type0-0-2=substring&type0-0-3=substring&value0-0-0=%2A&value0-0-1=%2A&value0-0-2=%2A&' +
            # 'value0-0-3=%2A&order=bug_status%2Cpriority%2Cassigned_to%2Cbug_id&limit=' + str(self.limit)
     ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)

        print("I GOT A BUG!!!!!!!!!!!!!!!!!!")

        #print(sel.css('tr[class~=bz_bugitem]'))

        for bug in sel.css('tr[class~=bz_bugitem]'):
            bid = bug.css('td[class~=first-child] > a::text').extract_first().strip()
            # b542518 > td.first-child.bz_id_column > a
            print("BID = " + str(bid))
            # b277140 > td.first-child.bz_id_column
            #yield {
            #    'text': quote.css("span.text::text").extract_first(),
            #    'author': quote.css("small.author::text").extract_first(),
            #    'tags': quote.css("div.tags > a.tag::text").extract()
            #}
        # b277140 > td.first-child.bz_id_column > a
        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
            if bid is not None:
                url = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + str(bid)
                yield scrapy.Request(url=url, callback=self.parseBug)

    def parseBug(self, response):
        sel = Selector(response)
        comment = sel.css('pre[class~=bz_comment_text]::text')
        print (comment)
        # pre[class~=bz_comment_text]::text'
