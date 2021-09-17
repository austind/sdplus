__version__ = "1.1"
# http://nbsvr241:8080/SetUpWizard.do?SkipNV2Filter=true&forwardTo=api

import requests
import json

class API(object):
    """
    The main sending class for the Manage Service Engine API
    """

    def __init__(self, api_token, sdplus_fqdn):
        self.api_url = f"https://{sdplus_fqdn}/api/v3/requests"
        self.session = requests.Session()
        self.session.headers.update({'authtoken': api_token})
        self.session.verify = False

    def _get_response(self, response):
        output = json.loads(response.text)
        if 400 <= response.status_code < 600:
            resp_stat = output.get('response_status')
            msgs = resp_stat.get('messages')
            if msgs:
                code = msgs[0]['status_code']
                msg = msgs[0].get('message')
                response.reason = f"SDP Error {code}"
                if msg:
                    response.reason = response.reason + f": {msg}"
        response.raise_for_status()
        return output


    def _get(self, params):
        endpoint = params.pop('endpoint')
        return self._get_response(self.session.get(endpoint))

    def _put(self, params):
        self.session.headers.update({"Accept": "application/vnd.manageengine.sdp.v3+json"})
        endpoint = params.pop('endpoint')
        data = {'request': params}
        return self._get_response(self.session.put(endpoint, data))


class Request(API):
    def __init__(self, api_token, sdplus_fqdn):
        API.__init__(self, api_token, sdplus_fqdn)

    # Add Request
    def add(
        self,
        subject,
        description,
        requester,
        requesteremail,
        impact="3 Impacts Department",
        urgency="3 Business Operations Slightly Affected",
        subcategory="Other",
        reqtemplate="Default Request",
        requesttype="Service Request",
        status="",
        mode="@Southmead Brunel building",
        service="CERNER",
        category="",
        group="Back Office Third Party",
        technician="",
        technicianemail="",
        item="",
        impactdetails="",
        resolution="",
        priority="",
        level="",
        supplier_ref="",
    ):
        params = {
            "operation": "addrequest",
            "subject": subject,
            "description": description,
            "requester": requester,
            "impact": impact,
            "urgency": urgency,
            "subcategory": subcategory,
            "requesteremail": requesteremail,
            "reqtemplate": reqtemplate,
            "requesttype": requesttype,
            "status": status,
            "mode": mode,  # =site
            "service": service,  # =Service Category
            "category": category,  #''=Self Service Incident
            "group": group,
            "technician": technician,
            "technicianemail": technicianemail,
            "item": item,
            "impactdetails": impactdetails,
            "resolution": resolution,
            "priority": priority,
            "level": level,
            "supplier ref": supplier_ref,
        }
        return self._send(params)

    # Update a call
    def update(
        self,
        id,
        display_id=None,
        subject=None,
        description=None,
        short_description=None,
        request_type=None,
        impact=None,
        impact_details=None,
        status=None,
        mode=None,
        level=None,
        urgency=None,
        priority=None,
        service_category=None,
        requester=None,
        department=None,
        assets=None,
        deleted_assets=None,
        deleted_on=None,
        deleted_by=None,
        site=None,
        group=None,
        technician=None,
        category=None,
        subcategory=None,
        item=None,
        on_behalf_of=None,
        service_approvers=None,
        template=None,
        request_template_task_ids=None,
        editor=None,
        email_ids_to_notify=None,
        update_reason=None,
        status_change_comments=None,
        created_time=None,
        due_by_time=None,
        first_response_due_by_time=None,
        project=None,
        request_initiated_change=None,
        problem=None,
        purchase_orders=None,
        parent_request_ids=None,
        child_request_ids=None,
        is_fcr=None,
        attachments=None,
        resources=None,
        udf_fields=None,
        resolution=None,
        content=None,
        add_to_linked_requests=None,
        closure_info=None,
        closure_code=None,
        requester_ack_resolution=None,
        requester_ack_comments=None,
        closure_comments=None,
        onhold_scheduler=None,
        scheduled_time=None,
        comments=None,
        change_to_status=None,
        linked_to_request=None,
        request=None
    ):
        """
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#edit-request
        """
        params = {
            'endpoint': f'{self.api_url}/{id}',
            "id": id,
            "display_id": display_id,
            "subject": subject,
            "description": description,
            "short_description": short_description,
            "request_type": request_type,
            "impact": impact,
            "impact_details": impact_details,
            "status": status,
            "mode": mode,
            "level": level,
            "urgency": urgency,
            "priority": priority,
            "service_category": service_category,
            "requester": requester,
            "department": department,
            "assets": assets,
            "deleted_assets": deleted_assets,
            "deleted_on": deleted_on,
            "deleted_by": deleted_by,
            "site": site,
            "group": group,
            "technician": technician,
            "category": category,
            "subcategory": subcategory,
            "item": item,
            "on_behalf_of": on_behalf_of,
            "service_approvers": service_approvers,
            "template": template,
            "request_template_task_ids": request_template_task_ids,
            "editor": editor,
            "email_ids_to_notify": email_ids_to_notify,
            "update_reason": update_reason,
            "status_change_comments": status_change_comments,
            "created_time": created_time,
            "due_by_time": due_by_time,
            "first_response_due_by_time": first_response_due_by_time,
            "project": project,
            "request_initiated_change": request_initiated_change,
            "problem": problem,
            "purchase_orders": purchase_orders,
            "parent_request_ids": parent_request_ids,
            "child_request_ids": child_request_ids,
            "is_fcr": is_fcr,
            "attachments": attachments,
            "resources": resources,
            "udf_fields": udf_fields,
            "resolution": resolution,
            "content": content,
            "add_to_linked_requests": add_to_linked_requests,
            "closure_info": closure_info,
            "closure_code": closure_code,
            "requester_ack_resolution": requester_ack_resolution,
            "requester_ack_comments": requester_ack_comments,
            "closure_comments": closure_comments,
            "onhold_scheduler": onhold_scheduler,
            "scheduled_time": scheduled_time,
            "comments": comments,
            "change_to_status": change_to_status,
            "linked_to_request": linked_to_request,
            "request": request
        }
        return self._put(params)

    def assign(self, work_order_id, technician):
        return self.update(work_order_id, technician=technician)

    def close(self, work_order_id, close_comments=""):
        params = {
            "operation": "CloseRequest",
            "workOrderID": work_order_id,
            "closecomment": close_comments,
        }
        return self._send(params)

    def delete(self, workorderid):  # get dictionary of a call's details
        params = {"operation": "deleterequest", "workOrderID": workorderid}
        return self._send(params)

    def add_note(self, workorderid, notesText, isPublic=True):
        params = {
            "operation": "AddNotes",
            "workOrderID": workorderid,
            "notesText": notesText,
            "isPublic": isPublic,  # True=public notes, False=private notes
        }
        return self._send(params)

    def add_work_log(
        self,
        workorderid,
        technician="",
        technicianemail="",
        description="",
        workhours="",
        workminutes="",
        cost="",
        executedtime="",
    ):
        params = {
            "operation": "AddNotes",
            "workOrderID": workorderid,
            "technician": technician,
            "technicianemail": technicianemail,
            "description": description,
            "workhours": workhours,
            "workminutes": workminutes,
            "cost": cost,
            "executedtime": executedtime,
        }
        return self._send(params)

    def delete_work_log(self, workorderid, workLogID=""):
        params = {
            "operation": "deleteworklog",
            "workOrderID": workorderid,
            "requestchargeid": workLogID,  # work Log ID to delete
        }
        return self._send(params)

    def get(self, id):
        params = {"endpoint": f"{self.api_url}/{id}"}
        return self._get(params)


class Requester(API):
    def __init__(self, username, password, domain, auth_type):
        # api_url = 'http://nbsvr241:8080/servlets/RequesterServlet'  # Test
        # api_url = 'http://sdplus/servlets/RequesterServlet'  # Live
        API.__init__(self, username, password, domain, auth_type, api_url)

    def add(
        self,
        name,
        employee_id="",
        description="",
        email="",
        phone="",
        mobile="",
        site="",
        department_name="",
        job_title="",
        request_view_permission="",
        approve_purchase_order="",
        login_name="",
        pwd="",
        udf_aliases={},  # {'udf_column_name_1': 'value1', 'udf_column_name_2': 'value2'}
    ):
        params = {
            "operation": "AddRequester",
            "name": name,
            "employeeId": employee_id,
            "description": description,
            "email": email,
            "phone": phone,
            "mobile": mobile,
            "site": site,
            "departmentName": department_name,
            "jobTitle": job_title,
            "requestViewPermission": request_view_permission,
            "approvePurchaseOrder": approve_purchase_order,
            "loginName": login_name,
            "pwd": pwd,
        }
        if udf_aliases:
            params.update(udf_aliases)
        return self._send(params)

    def update(
        self,
        req_login_name,
        req_domain_name="",
        req_user_name="",
        req_email_id="",
        name="",
        user_id="",
        employee_id="",
        email="",
        phone="",
        mobile="",
        sms_mail_id="",
        site="",
        department_name="",
        job_title="",
        request_view_permission="",
        approve_purchase_order="",
        udf_aliases={},  # {'udf_column_name_1': 'value1', 'udf_column_name_2': 'value2'}
    ):
        params = {
            "operation": "UpdateRequester",
            "reqLoginName": req_login_name,
            "reqDomainName": req_domain_name,
            "reqUserName": req_user_name,
            "reqEmailId": req_email_id,
            "name": name,
            "userid": user_id,
            "employeeId": employee_id,
            "email": email,
            "phone": phone,
            "mobile": mobile,
            "smsMailId": sms_mail_id,
            "site": site,
            "departmentName": department_name,
            "jobTitle": job_title,
            "requestViewPermission": request_view_permission,
            "approvePurchaseOrder": approve_purchase_order,
        }
        if udf_aliases:
            params.update(udf_aliases)
        return self._send(params)

    def delete(
        self,
        req_login_name="",
        req_user_name="",
        req_domain_name="",
        req_email_id="",
        user_id="",
        username="",
        password="",
    ):
        params = {
            "operation": "DeleteRequester",
            "reqLoginName": req_login_name,
            "reqUserName": req_user_name,
            "reqDomainName": req_domain_name,
            "reqEmailId": req_email_id,
            "userid": user_id,
            "username": username,
            "password": password,
        }
        return self._send(params)

