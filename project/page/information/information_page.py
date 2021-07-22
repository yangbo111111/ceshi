"""
created: 202008011 by yb
description: 信息模块元素库
Modification History:
1、2020-8-11 yb创建了此文件
"""

from poium import Page, PageElement,NewPageElement


class Information_page(Page):
    # 登录页面
    username = NewPageElement(name="username", describe="用户名输入框")
    password = NewPageElement(id_='password', describe="账号输入框")
    login_button = NewPageElement(xpath="//*[@id='container']/div[3]/div/div[1]/div[2]/form/button", describe="登录按钮")
    # 公共元素
    add_button = NewPageElement(xpath="//*[@id='addNew']", describe="新建按钮")
    choice_all = NewPageElement(xpath="//input[@name='btSelectAll']", describe="全选框")
    choice_frist_data = NewPageElement(xpath="//tr[1]//td[1]//input[1]", describe="第一个选择框")
    delete_button = NewPageElement(xpath="//a[@class='Item-Remove ml-5']", describe="删除按钮")
    batch_deletion_button = NewPageElement(link_text="批量删除", describe="批量删除按钮")
    ok_button = NewPageElement(class_name="layui-layer-btn0", describe="确定按钮")
    edit_button = NewPageElement(xpath="//i[@class='fa fa-edit']", describe="编辑按钮")
    frist_data = NewPageElement(xpath="//tr[1]//td[2]//a[1]", describe="第一条记录")
    no_query_result = NewPageElement(xpath="//tr[@class='no-records-found']//span[@class='i18n']", describe="无搜索结果")
    no_data = NewPageElement(xpath="//tr[@class='no-records-found']//span[@class='i18n']", describe="暂无数据")
    # 首页
    head_portrait = NewPageElement(xpath="//a[@class='dropdown-toggle user-menu']", describe="右上角头像")
    sign_out = NewPageElement(xpath="//li[@class='ez-person-footer']", describe="安全退出")
    login_name = NewPageElement(xpath="//a[@class='dropdown-toggle user-menu']//span[2]", describe="登录人姓名")
    enter_base = NewPageElement(xpath="//div[@class='right clearfix']//li[4]//a[1]", describe="进入后台")
    enter_office = NewPageElement(xpath="//li[@class='dropdown']//li[1]//a[1]", describe="进入前台")
    # 信息菜单
    information = NewPageElement(link_text="信息", describe="信息菜单")
    Column_management = NewPageElement(xpath="//*[@id='main-menu-inner']/ul/li/ul/li[2]/a/span", describe="栏目管理菜单")
    content_template = NewPageElement(xpath="//*[@id='main-menu-inner']/ul/li/ul/li[4]/a/span", describe="内容模板菜单")
    column_content = NewPageElement(link_text="栏目内容", describe="栏目内容菜单")
    my_content = NewPageElement(link_text="我的内容", describe="我的内容菜单")
    drafts = NewPageElement(link_text="草稿箱", describe="草稿箱菜单")
    my_post = NewPageElement(link_text="我的发布", describe="我的发布菜单")
    information_statistics = NewPageElement(link_text="信息统计", describe="信息统计菜单")
    # 栏目管理
    base_infomation = NewPageElement(id_="basicInfoPage", describe="基本信息页签")
    details = NewPageElement(id_="detailInfoPage", describe="详细设置页签")
    column_name = NewPageElement(xpath="//input[@id='name']", describe="栏目名称")
    column_code = NewPageElement(id_="columnCode", describe="栏目编码")
    column_describe = NewPageElement(xpath="//*[@id='comment']", describe="描述")
    allownow_button = NewPageElement(id_="columnCreateLimit", describe="允许新建选择按钮")
    column_save_button = NewPageElement(xpath="//div[@id='new-div0']//button[@id='setAf']", describe="新增保存按钮")
    column_modifysave_button = NewPageElement(xpath="//div[@id='editColumnBtnDiv0']//button[@id='setAf']", describe="修改页面保存按钮")
    first_column = PageElement(id_="cmsColumnTree_1_span", describe="第一个栏目")
    column_delete_button = NewPageElement(xpath="//div[@id='content-wrapper']//a[4]", describe="栏目删除按钮")
    column_query = NewPageElement(id_="searchTreeData2", describe="查询框")
    column_no_search = NewPageElement(xpath="//p[@id='isShow_p']", describe="无搜索结果")
    # 选人页面
    largest_organization = NewPageElement(xpath="//span[@id='cmpOrgTree_1_check']", describe="最大组织")
    largest_organization_name = NewPageElement(xpath="//span[@id='cmpOrgTree_1_span']//span", describe="最大组织名称")
    pick_ok_button = NewPageElement(xpath="//*[@id='judgColumnCreateRangespopuModals']/div[3]/button", describe="确定按钮")

    # 内容模板页面
    add_category_button = NewPageElement(xpath="//*[@id='tid_column-nav']/button", describe="新建类别按钮")
    first_category = PageElement(id_='orgTree11_1_span', describe="左侧树第一个类别")
    category_edit_button = NewPageElement(xpath="//a[@id='edit']", describe="类别编辑按钮")
    category_delete_button = NewPageElement(id_="deleteColumn", describe="类别删除按钮")
    template_add_button = NewPageElement(id_="addNew", describe="模板新建按钮")
    template_modify_button = NewPageElement(xpath="//tr[1]//td[6]//a[1]//i[1]" , describe="模板修改按钮")
    template_delete_button = NewPageElement(xpath="//tr[1]//td[6]//a[2]//i[1]", describe="模板删除按钮")
    category_name_query = NewPageElement(xpath="//*[@id='searchTreeData2']", describe="类别名称查询框")
    choice_frist_template = NewPageElement(xpath="//tr[1]//td[1]//input[1]", describe="第一个模板选择框")
    frist_template_name = NewPageElement(xpath="//tr[1]//td[2]//a[1]", describe="第一个模板名称")
    template_query_name = NewPageElement(xpath="//input[@placeholder='请输入']", describe="模板名称查询框")
    template_query_button = NewPageElement(xpath="//*[@id='createdSearchbar']/div/form/div/div[2]/input[1]", describe="搜索按钮")
    template_no_search = NewPageElement(xpath="//*[@id='s-table']/tbody/tr/td/span", describe="无模板搜索结果")
    category_no_search = NewPageElement(xpath="//*[@id='isShow_p']", describe="无类别搜索结果")
    # 新建类别页面
    category_name = NewPageElement(xpath="//input[@id='name']", describe="类别名称")
    category_describe = NewPageElement(id_="description", describe="类别描述")
    add_category_save_button = NewPageElement(xpath="//*[@id='addCateModal']/div[3]/button", describe="新增类别保存按钮")
    add_category_close_button = NewPageElement(xpath="//*[@id='addCateModal']/div[1]/span[2]", describe="新增类别关闭按钮")
    # 修改类别页面
    modify_category_save_button = NewPageElement(xpath="//*[@id='editCateModal']/div[3]/button", describe="修改类别保存按钮")
    modify_category_close_button = NewPageElement(xpath="//*[@id='editCateModal']/div[1]/span[2]", describe="修改类别关闭按钮")
    # 新增模板页面
    template_name = NewPageElement(xpath="//input[@id='name']", describe="模板名称")
    category_dropdown_button = NewPageElement(xpath="//*[@id='templateType']/div/span", describe="类别下拉按钮")
    dropdown_first_category = NewPageElement(xpath="//div[@id='templateType']//span[@id='treeselecttypeId_2_check']", describe="类别下拉第一个类别")
    template_content = NewPageElement(xpath="//body[@class='view']", describe="内容")
    add_template_save_button = NewPageElement(xpath="//*[@id='addModal']/div[3]/button", describe="模板保存按钮")
    add_template_close_button = NewPageElement(xpath="//*[@id='addModal']/div[1]/span[2]", describe="模板关闭按钮")
    # 修改模板页面
    modify_template_close_button = NewPageElement(xpath="//*[@id='editModal']/div[1]/span[2]", describe="修改模板关闭按钮")
    modify_template_save_button = NewPageElement(xpath="//*[@id='editModal']/div[3]/button", describe="修改模板保存按钮")
    # 查看模板页面
    see_template_name = NewPageElement(xpath="//*[@id='eaCategory']/h4",describe="查看页面模板名称")
    see_template_close_button = NewPageElement(xpath="//*[@id='viewModal']/div[1]/span[2]", describe="查看页面关闭按钮")

    # 栏目内容列表
    information_batch_move_button = NewPageElement(id_="move", describe="批量移动按钮")
    information_batch_copy_button = NewPageElement(link_text="批量复制", describe="批量复制按钮")
    information_topping_button = NewPageElement(xpath="//tr[1]//td[8]//div[1]//a[2]", describe="置顶按钮")
    information_topping_fix_button = NewPageElement(xpath="//a[@class='layui-layer-btn0']", describe="置顶确定按钮")
    information_essence_button = NewPageElement(xpath="//tr[1]//td[8]//div[1]//a[3]", describe="精华按钮")
    information_topping_sign = NewPageElement(xpath="//i[@class='iconfont icon-top i18n']", describe="置顶标记")
    information_essence_sign = NewPageElement(xpath="//i[@class='iconfont icon-essence i18n']", describe="精华标记")
    information_modify_button = NewPageElement(xpath="//i[@class='fa fa-edit']", describe="信息编辑按钮")
    information_delete_button = NewPageElement(xpath="//a[@class='Item-Remove ml-4 i18n']", describe="信息删除按钮")
    information_frist_column = NewPageElement(id_="cmsColumnTree_1_span", describe="第一个栏目")
    information_query_name = NewPageElement(xpath="//div[@class='col-sm-6 no-padding show']//input[@placeholder='请输入']", describe="信息标题查询")
    information_query_button = NewPageElement(xpath="//button[@class='btn btn-primary pull-left mr-5 i18n']", describe="搜索按钮")
    information_frist_name = NewPageElement(xpath="//td[contains(@class,'infotitle')]//a", describe="第一个信息名称")
    choice_frist_information = NewPageElement(xpath="//*[@id='s-table']/tbody/tr[1]/td[1]/input", describe="第一条信息选择框")
    information_eliminate_button = NewPageElement(xpath="//button[@class='btn btn-default pull-left i18n']", describe="清除按钮")
    no_information_query_result = NewPageElement(xpath="//tr[@class='no-records-found']//span[@class='i18n']", describe="无搜索结果")
    success_tips = NewPageElement(xpath="//div[@class='layui-layer-content layui-layer-padding']", describe="成功提示语")
    # 新建信息页面
    information_name = NewPageElement(xpath="//*[@id='40288819675965b60167597293510027field']/div[1]/input", describe="信息标题")
    information_content = NewPageElement(xpath="//body[@class='view']", describe="信息内容")
    information_more_settings = NewPageElement(xpath="//*[@id='nvaTab']/li[2]/a", describe="更多设置")
    information_save_button = NewPageElement(xpath="//div[@class='modal-footer']//button[2]", describe="发布按钮")
    infromaton_close_button = NewPageElement(xpath="//*[@id='runtimeModalAddModal']/div[1]/span[2]", describe="新建页面关闭按钮")
    # 编辑信息页面
    modify_information_save_button = NewPageElement(xpath="//*[@id='runtimeModalEditModal']/div[3]/button", describe="信息保存按钮")
    modify_information_close_button = NewPageElement(xpath="//*[@id='runtimeModalEditModal']/div[1]/span[2]/i", describe="编辑信息页面关闭按钮")
    # 信息查看页面
    see_information_title = NewPageElement(xpath="//h3[@class='text-left']//strong", describe="查看页面标题")
    see_information_close_button = NewPageElement(xpath="//*[@id='viewModal']/div[1]/span[2]", describe="信息查看页面关闭按钮")
    # 选择栏目页面
    column_choice_frist_column = NewPageElement(id_="columnTreesel_1_check", describe="第一个栏目选择框")
    column_choice_frist_column_name = NewPageElement(id_="columnTreesel_1_span", describe="第一个栏目")
    copy_column_choice_save_button = NewPageElement(xpath="//*[@id='copyColumnModel']/div[3]/button", describe="复制栏目选择保存按钮")
    move_column_choice_save_button = NewPageElement(xpath="//*[@id='moveColumnModel']/div[3]/button", describe="移动栏目选择保存按钮")
    sync_column_choice_save_button = NewPageElement(xpath="//*[@id='syncColumnModel']/div[3]/button", describe="同步栏目选择保存按钮")
    column_choice_query = NewPageElement(id_="searchTreeData", describe="栏目查询框")
    column_choice_query_button = NewPageElement(xpath="//div[@class='modal-body thin-scroll']//i[@class='fa fa-search']", describe="栏目查询按钮")
    column_choice_close_button = NewPageElement(xpath="//*[@id='copyColumnModel']/div[1]/span[2]", describe="栏目选择页面关闭按钮")

    # 我的内容
    drafts_release_button = NewPageElement(xpath="//div[@class='fixed-table-container']//a[2]", describe="发布按钮")
    drafts_batch_release_button = NewPageElement(link_text="批量发布", describe="批量发布按钮")
    drafts_delete_button = NewPageElement(xpath="//a[@class='Item-Remove ml-5 i18n']", describe="草稿箱信息删除按钮")
    my_information_frist_name = NewPageElement(xpath="//tr[1]//td[2]//a[1]", describe="第一条信息")
    my_modify_information_save_button = NewPageElement(xpath="//*[@id='runtimeModaleditModal']/div[3]/button[1]", describe="信息编辑页面保存按钮")
    my_post_delete_button = NewPageElement(xpath="//a[@class='Item-Remove ml-10 i18n']", describe="我的发布信息删除按钮")
    my_post_synchronization_button = NewPageElement(xpath="//tr[1]//td[6]//a[2]", describe="我的发布同步按钮")
    my_post_copy_button = NewPageElement(xpath="//tr[1]//td[6]//a[3]", describe="我的发布复制按钮")
    my_post_move_button = NewPageElement(xpath="//tr[1]//td[6]//a[4]", describe="我的发布移动按钮")

    # 信息统计
    statistics_publish_publisher_query = NewPageElement(id_="issuerName", describe="发布量页签发布人查询框")
    statistics_essence_publisher_query = NewPageElement(xpath="//input[@id='issuerNameE']", describe="精华量页签发布人查询框")
    publish_statistics = NewPageElement(link_text="发布量统计", describe="发布量统计页签")
    essence_statistics = NewPageElement(link_text="精华量统计", describe="精华量统计页签")
    publish_first_publisher_name = NewPageElement(xpath="//*[@id='s-table']/tbody/tr/td[2]", describe="发布页签第一个发布人名称")
    essence_first_publisher_name = NewPageElement(xpath="//*[@id='s-table1']/tbody/tr/td[2]", describe="精华页签第一个发布人名称")
    publish_release = NewPageElement(xpath="//*[@id='s-table']/tbody/tr/td[3]", describe="发布页签发布数量")
    essence_release = NewPageElement(xpath="//*[@id='s-table1']/tbody/tr/td[3]", describe="精华页签发布数量")
    essence_statistics_number = NewPageElement(xpath="//*[@id='s-table1']/tbody/tr[1]/td[3]", describe="精华数量")
    release_query_button = NewPageElement(xpath="//div[@id='publish_statistics']//form[contains(@class,'form-horizontal ez-searchbar-complex ez-form-fold')]//button[1]",
                                          describe="发布页签搜索按钮")
    essence_query_button = NewPageElement(xpath="//button[contains(@class,'btn btn-primary pull-left mr-5 i18n')]", describe="精华页签搜索按钮")
    release_query_open_button = NewPageElement(xpath="//div[@id='publish_statistics']//div[@class='ez-form-foldbtn']", describe="发布页签展开按钮")
    essence_query_open_button = NewPageElement(xpath="//div[@id='essence_statistics']//div[@class='ez-form-foldbtn']", describe="精华页签展开按钮")

    # 后台首页
    content_center = NewPageElement(id_="402887f859b694e00159b699ab6e0001", describe="内容中心菜单")

    # 内容中心菜单
    channel_management = NewPageElement(link_text="频道管理", describe="频道管理菜单")
    channel_template = NewPageElement(link_text="频道模板", describe="频道模板菜单")
    virtual_column = NewPageElement(link_text="虚拟栏目", describe="虚拟栏目菜单")
    field_management = NewPageElement(link_text="字段管理", describe="字段管理菜单")
    unit_channel = NewPageElement(link_text="单位频道", describe="字段管理菜单")
    # 频道管理
    channel_management_query = NewPageElement(xpath="//input[@placeholder='请输入']", describe="频道名称查询框")
    channel_management_query_button = NewPageElement(id_="channleSerchBtn", describe="搜索按钮")
    channel_delete_button = NewPageElement(xpath="//a[@class='Item-Remove ml-5']", describe="删除按钮")
    channel_management_design_button = NewPageElement(xpath="//*[@id='channel-table']/tbody/tr[1]/td[6]/a[2]", describe="设计按钮")
    channel_management_publish_button = NewPageElement(xpath="//tr[1]//td[6]//a[4]", describe="发布按钮")
    # 新建频道页面
    channel_name = NewPageElement(id_="name", describe="频道名称")
    channel_code = NewPageElement(id_="channelCode", describe="频道编码")
    add_channel_save_button = NewPageElement(xpath="//div[@id='addModal']//button[@class='btn radius btn-primary']", describe="新建保存按钮")
    add_channel_close_button = NewPageElement(xpath="//div[@id='addModal']//span[@class='modal-close']", describe="关闭按钮")
    # 编辑频道页面
    edit_channel_save_button = NewPageElement(xpath="//div[@id='editModal']//button[@class='btn radius btn-primary']", describe="编辑保存按钮")
    edit_channel_close_button = NewPageElement(xpath="//div[@id='editModal']//span[@class='modal-close']", describe="编辑关闭按钮")
    # 查看频道页面
    see_channel_name = NewPageElement(xpath="//div[@class='form-horizontal ez-form-horizontal']//div[1]//div[1]//div[1]//p[1]", describe="频道名称")
    see_channel_close_button = NewPageElement(xpath="//div[@id='viewModal']//span[@class='modal-close']", describe="查看关闭按钮")
    # 设计频道页面
    design_channel_basics = NewPageElement(xpath="//*[@id='designModal']/div[2]/div[1]/ul/li[1]/a", describe="基础设置页签")
    design_channel_field = NewPageElement(xpath="//*[@id='designModal']/div[2]/div[1]/ul/li[2]/a", describe="列表字段设置页签")
    design_channel_add_button = NewPageElement(xpath="//div[@id='list-tableToolbar']//a[@id='addNew']", describe="字段添加按钮")
    design_channel_close_button = NewPageElement(xpath="//*[@id='designModal']/div[1]/span[2]", describe="关闭按钮")
    design_channel_query = NewPageElement(xpath="//div[@class='col-lg-9 col-sm-8']//input[@placeholder='请输入']", describe="字段名称查询框")
    design_channel_query_button = NewPageElement(xpath="//div[@id='createdFieldSearchbar']//input[@class='btn btn-primary btn']", describe="搜索按钮")
    design_channel_clear_button = NewPageElement(xpath="//div[@id='createdFieldSearchbar']//input[@class='btn btn-default btn']", describe="清除按钮")
    design_channel_frist_field = NewPageElement(xpath="//div[@class='modal-scrollable']//tr[1]//td[2]//a[1]", describe="第一条字段名称")
    design_channel_edit_button = NewPageElement(xpath="//*[@id='list-table']/tbody/tr[1]/td[7]/a[1]", describe="编辑按钮")
    design_channel_delete_button = NewPageElement(xpath="//tr[1]//td[7]//a[2]", describe="删除按钮")
    design_channel_batch_deletion_button = NewPageElement(xpath="//div[@id='list-tableToolbar']//a[contains(@class,'btn btn-danger')]", describe="批量删除按钮")
    design_channel_choice_all = NewPageElement(xpath="//table[@id='list-table']//input[@name='btSelectAll']", describe="全选按钮")
    design_channel_choice_form_down_button = NewPageElement(xpath="//div[@class='input-group']//span[@class='input-group-addon']", describe="选择表单下拉按钮")
    design_channel_choice_form = NewPageElement(xpath="//div[@class='ez-selectBar-search']//span[@id='treeselectuseTableName_1_span']", describe="选择表单")
    design_channel_save_button = NewPageElement(xpath="//*[@id='designModal']/div[3]/button", describe="保存按钮")
    # 新增字段页面
    add_field_chose_frist_field = NewPageElement(xpath="//li[@class='ui-selectee ui-selected']", describe="选择左边第一个字段")
    add_field_shift_right_button = NewPageElement(xpath="//*[@id='eaChannel']/div[3]/div[2]/div/button[1]", describe="字段右移按钮")
    add_field_close_button = NewPageElement(xpath="//*[@id='addFieldModal']/div[1]/span[2]", describe="页面关闭按钮")
    add_field_frist_field = NewPageElement(xpath="//ul[@id='list-selectBar-left']//li[1]", describe="可选第一个字段")
    add_field_save_button = NewPageElement(xpath="//div[@id='addFieldModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    # 编辑字段页面
    edit_field_title = NewPageElement(id_="name", describe="标题框")
    edit_field_close_button = NewPageElement(xpath="//*[@id='editFieldModal']/div[1]/span[2]", describe="页面关闭按钮")
    edit_field_save_button = NewPageElement(xpath="//*[@id='editFieldModal']/div[3]/button", describe="保存按钮")

    # 频道模板列表
    channel_template_query_button = NewPageElement(xpath="//input[@class='btn btn-primary btn']", describe="搜索按钮")
    channel_template_name_query = NewPageElement(xpath="//input[@placeholder='请输入']", describe="模板名称")
    channel_template_edit_button = NewPageElement(xpath="//div[@class='fixed-table-container']//a[2]", describe="修改按钮")
    channel_template_design_button = NewPageElement(xpath="//tr[1]//td[6]//a[3]//i[1]", describe="设计按钮")
    channel_template_preview_button = NewPageElement(xpath="//tr[1]//td[6]//a[1]", describe="预览按钮")
    # 新增频道模板页面
    add_channel_template_name = NewPageElement(xpath="//input[@id='name']", describe="模板名称")
    add_channel_template_code = NewPageElement(xpath="//input[@id='code']", describe="模板编码")
    add_channel_template_save_button = NewPageElement(xpath="//div[@id='addModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    add_channel_template_close_button = NewPageElement(xpath="//div[@id='addModal']//span[@class='modal-close']", describe="页面关闭按钮")
    # 编辑频道模板页面
    edit_channel_template_save_button = NewPageElement(xpath="//div[@id='editModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    edit_channel_template_close_button = NewPageElement(xpath="//div[@id='editModal']//span[@class='modal-close']", describe="页面关闭按钮")
    # 查看频道模板页面
    see_channel_template_name = NewPageElement(xpath="//*[@id='eaChannel']/div/div[1]/div[1]/div/p", describe="模板名称")
    see_channel_template_close_button = NewPageElement(xpath="//div[@id='viewModal']//span[@class='modal-close']", describe="页面关闭按钮")
    # 设计频道模板页面
    design_channel_template_save_button = NewPageElement(xpath="//input[@id='saveCode']", describe="保存按钮")
    design_channel_template_close_button = NewPageElement(xpath="//div[@id='designModal']//span[@class='modal-close']", describe="关闭按钮")
    # 预览频道模板页面
    preview_channel_template_name = NewPageElement(xpath="//div[@id='showModal']//h3[@id='dialogName']", describe="预览页面名称")
    preview_channel_template_close_button = NewPageElement(xpath="//div[@id='showModal']//span[contains(@class,'modal-close')]", describe="关闭按钮")

    # 虚拟栏目页面
    virtual_column_name = NewPageElement(id_="name", describe="栏目名称")
    virtual_column_relation_column_button = NewPageElement(xpath="//span[@class='input-group-addon input-file-preview ez-openbtn']", describe="关联栏目选择按钮")
    relation_column_chose_column = NewPageElement(xpath="//span[@id='columnPorleTree_1_span']", describe="关联栏目页面选择第一个栏目")
    virtual_column_save_button = NewPageElement(xpath="//button[@id='setAf']", describe="保存按钮")
    virtual_column_lower_column = NewPageElement(id_="vcperTab", describe="下级栏目")
    virtual_column_frist_column = PageElement(id_="virtualColumnTree_1_span", describe="左侧第一个栏目")
    virtual_column_delete_column = NewPageElement(xpath="//li[@id='virtualColumnDelete']//a[@class='navitem']", describe="栏目树删除按钮")
    virtual_column_query = NewPageElement(id_="searchTree", describe="左侧栏目树查询")
    virtual_column_query_button = NewPageElement(xpath="//i[@class='fa fa-search']", describe="左侧查询按钮")
    virtual_column_add_lower_column = NewPageElement(id_="addSub();", describe="新建下级栏目")
    virtual_column_no_query = NewPageElement(xpath="//p[@id='isShow_text']", describe="栏目树无查询结果")
    # 下级栏目页面
    lower_virtual_add_button = NewPageElement(xpath="//a[@id='addNew']", describe="新建按钮")
    lower_virtual_edit_button = NewPageElement(xpath="//td[5]//a[1]", describe="编辑按钮")
    lower_virtual_delete_button = NewPageElement(xpath="//div[@class='fixed-table-container']//a[2]", describe="删除按钮")
    lower_virtual_chose_frist_data = NewPageElement(xpath="//input[@name='btSelectItem']", describe="选择第一条记录")
    lower_virtual_move_button = NewPageElement(xpath="//a[contains(@class,'btn btn-default')]", describe="批量移动按钮")
    # 新建下级虚拟栏目页面
    lower_virtual_column_name = NewPageElement(xpath="//body/div/div/div/div/form/div[1]/div[1]/input[1]", describe="栏目名称")
    lower_virtual_column_chose_button = NewPageElement(xpath="//body/div/div/div/div/form/div/div/div/div/span[2]", describe="选择关联栏目按钮")
    lower_virtual_column_save_button = NewPageElement(xpath="//*[@id='editNextModal']/div[3]/button", describe="保存按钮")
    lower_virtual_column_close_button = NewPageElement(xpath="//*[@id='editNextModal']/div[1]/span[2]", describe="关闭按钮")
    # 修改下级虚拟栏目页面
    edit_lower_virtual_column_name = NewPageElement(xpath="//body/div/div/div/div/form/div[1]/div[1]/input[1]", describe="修改页面栏目名称")
    edit_lower_virtual_column_save_button = NewPageElement(xpath="//*[@id='editNextModal']/div[3]/button", describe="保存按钮")
    edit_lower_virtual_column_close_button = NewPageElement(xpath="//*[@id='editNextModal']/div[1]/span[2]", describe="关闭按钮")
    # 关联栏目页面
    connected_column_query = NewPageElement(xpath="//input[@id='searchTreeData']", describe="栏目查询")
    connected_column_query_button = NewPageElement(xpath="//div[@id='user-add-body']//span[@class='search-icon']", describe="查询按钮")
    connected_column_close_button = NewPageElement(xpath="/html/body/div[8]/div/div[1]/span[2]",
                                                   describe="页面关闭按钮")
    connected_column_frist_column = NewPageElement(xpath="//span[@id='columnPorleTree_1_span']", describe="第一个栏目")
    connected_column_save_button = NewPageElement(xpath="/html/body/div[8]/div/div[3]/button", describe="保存按钮")
    # 查看下级栏目页面
    see_lower_virtual_column_name = NewPageElement(xpath="//div[@class='form-horizontal ez-form-horizontal']//div[1]//div[1]//div[1]//p[1]",
                                               describe="栏目名称")
    see_lower_virtual_close_button = NewPageElement(xpath="//div[@id='viewModal']//span[@class='modal-close']", describe="查看页面关闭按钮")
    # 下级移动选择栏目页面
    move_lower_virtual_column_query = NewPageElement(xpath="//input[@placeholder='快速查找栏目']", describe="查询框")
    move_lower_virtual_column_query_button = NewPageElement(xpath="//div[@class='modal-body thin-scroll']//div//span[@class='search-icon']",
                                                            describe="查询按钮")
    move_lower_virtual_column_frist_column = NewPageElement(xpath="//span[@id='selectTree_1_span']", describe="第一个栏目")
    move_lower_virtual_column_close_button = NewPageElement(xpath="//div[@id='selectModal']//span[@class='modal-close']", describe="关闭按钮")
    move_lower_virtual_column_save_button = NewPageElement(xpath="//div[@id='selectModal']//button[@class='btn radius btn-primary']", describe="保存按钮")

    # 字段管理
    field_management_add_button = NewPageElement(xpath="//a[@class='btn btn-primary']", describe="新建按钮")
    field_management_edit_button = NewPageElement(xpath="//tr[1]//td[7]//div[1]//a[2]", describe="编辑按钮")
    field_management_copy_button = NewPageElement(xpath="//tr[1]//td[7]//div[1]//a[3]", describe="复制按钮")
    field_management_sync_button = NewPageElement(xpath="//tr[1]//td[7]//div[1]//a[1]", describe="同步按钮")
    field_management_batch_sync_button = NewPageElement(link_text="批量同步", describe="批量同步按钮")
    field_management_field_setup_button = NewPageElement(xpath="//tr[1]//td[7]//div[1]//a[4]", describe="字段设置按钮")
    field_management_delete_button = NewPageElement(xpath="//tr[1]//td[7]//div[1]//a[5]", describe="删除按钮")
    field_management_data_name = NewPageElement(xpath="//tr[1]//td[2]//a[1]", describe="数据表名称")
    field_management_query = NewPageElement(xpath="//input[@placeholder='请输入数据表或系统名称']", describe="列表查询框")
    field_management_query_button = NewPageElement(xpath="//button[@class='btn btn-primary mr-5 pull-left ml-15']", describe="搜索按钮")
    field_management_clear_button = NewPageElement(xpath="//button[@class='btn btn-default']",
                                                   describe="清除按钮")
    # 新建数据表
    field_management_add_data_sheet_name = NewPageElement(xpath="//input[@id='tblNameCn']", describe="数据表名称")
    field_management_add_data_sheet_system_name = NewPageElement(xpath="//input[@id='tblName']", describe="系统名称")
    field_management_add_data_sheet_dropdown_button = NewPageElement(xpath="//span[@id='select_span']", describe="下拉按钮")
    field_management_add_data_sheet_chose_classification = NewPageElement(xpath="//span[@id='select_cate_1_span']", describe="选择内容管理")
    field_management_add_data_sheet_close_button = NewPageElement(xpath="//div[@id='addModal']//span[@class='modal-close']", describe="关闭按钮")
    field_management_add_data_sheet_save_button = NewPageElement(xpath="//div[@id='addModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    # 编辑数据表
    field_management_edit_data_sheet_name = NewPageElement(xpath="//input[@id='tblNameCn']", describe="数据表名称")
    field_management_edit_data_sheet_close_button = NewPageElement(
        xpath="//div[@id='contentEditModal']//span[@class='modal-close']", describe="关闭按钮")
    field_management_edit_data_sheet_save_button = NewPageElement(
        xpath="//div[@id='contentEditModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    # 查看数据表
    field_management_view_data_sheet_name = NewPageElement(xpath="//div[@id='viewModal']//div[1]//div[1]//p[1]", describe="数据表名称")
    field_management_view_data_sheet_close_button = NewPageElement(xpath="//div[@class='modal-scrollable']//span[@class='modal-close']",
                                                                   describe="关闭按钮")
    # 字段设置
    field_setup_name = NewPageElement(xpath="//*[@id='fieldTbl-table']/tbody/tr/td[2]/a", describe="字段名称")
    field_setup_sync_button = NewPageElement(xpath="//tr[1]//td[9]//div[1]//a[1]", describe="同步按钮")
    field_setup_edit_button = NewPageElement(xpath="//div[@class='operate-btns']//a[1]", describe="编辑按钮")
    field_setup_delete_button = NewPageElement(xpath="//div[@class='operate-btns']//a[3]", describe="删除按钮")
    field_setup_attribute_button = NewPageElement(xpath="//div[@class='operate-btns']//a[2]", describe="属性设置按钮")
    field_setup_batch_add_button = NewPageElement(link_text="批量新建", describe="批量新建按钮")
    field_setup_batch_edit_button = NewPageElement(link_text="批量编辑", describe="批量编辑按钮")
    field_setup_query = NewPageElement(xpath="//input[@placeholder='请输入字段或系统名称']", describe="列表查询框")
    # 新建字段
    field_setup_field_name = NewPageElement(id_="fieldNameCn", describe="字段名称输入框")
    field_setup_add_field_close_button = NewPageElement(xpath="//div[@id='addModal']//span[@class='modal-close']", describe="关闭按钮")
    field_setup_add_field_save_button = NewPageElement(xpath="//div[@id='addModal']//button[@class='btn radius btn-primary']",
                                                        describe="保存按钮")
    # 编辑字段页面
    field_setup_edit_field_close_button = NewPageElement(xpath="//div[@id='fieldEditModal']//span[@class='modal-close']",
                                                        describe="关闭按钮")
    field_setup_edit_field_save_button = NewPageElement(xpath="//div[@id='fieldEditModal']//button[@class='btn radius btn-primary']",
        describe="保存按钮")
    # 查看字段页面
    field_setup_view_field_name = NewPageElement(xpath="//*[@id='vueFormFieldTbl']/div[1]/div[1]/p", describe="字段名称")
    field_setup_view_field_close_button = NewPageElement(xpath="//div[@class='modal-scrollable']//span[@class='modal-close']",
                                                        describe="关闭按钮")
    # 属性设置页面
    field_setup_attribute_close_button = NewPageElement(xpath="//*[@id='fieldAttrEditModal']/div[1]/span[2]", describe="关闭按钮")
    # 批量新建字段页面
    field_setup_batch_field_name = NewPageElement(xpath="//input[@placeholder='1-20个字符，中文/字母/数字/符号']", describe="字段名称输入框")
    field_setup_batch_add_field_save_button = NewPageElement(xpath="//*[@id='batchAddModal']/div[3]/button", describe="保存按钮")
    field_setup_batch_add_field_close_button = NewPageElement(xpath="//*[@id='batchAddModal']/div[1]/span",
                                                             describe="关闭按钮")
    # 批量修改字段页面
    field_setup_batch_edit_field_save_button = NewPageElement(xpath="//*[@id='batchEditModal']/div[3]/button",
                                                             describe="保存按钮")
    field_setup_batch_edit_field_close_button = NewPageElement(xpath="//*[@id='batchEditModal']/div[1]/span",
                                                              describe="关闭按钮")

    # 单位频道列表
    unit_channel_batch_add_button = NewPageElement(xpath="//a[@id='addNew']", describe="批量新建按钮")
    unit_channel_preview_button = NewPageElement(xpath="//tr[1]//td[7]//a[1]", describe="预览按钮")
    unit_channel_edit_button = NewPageElement(xpath="//tr[1]//td[7]//a[2]", describe="编辑按钮")
    unit_channel_design_button = NewPageElement(xpath="//tr[1]//td[7]//a[3]", describe="设计按钮")
    unit_channel_unpublish_button = NewPageElement(xpath="//tr[1]//td[7]//a[4]", describe="取消发布按钮")
    unit_channel_delete_button = NewPageElement(xpath="//tr[1]//td[7]//a[5]", describe="删除按钮")
    unit_channel_release_state = NewPageElement(xpath="//tr[1]//td[6]", describe="发布状态")
    unit_channel_name_query = NewPageElement(xpath="//div[@class='refine-search']//div[1]//div[1]//div[1]//input[1]", describe="频道名称查询")
    unit_channel_name_query_button = NewPageElement(xpath="//button[@id='channleSerchBtn']", describe="查询按钮")
    # 新建单位频道页面
    add_unit_channel_save_buton = NewPageElement(xpath="//div[@id='addModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    add_unit_channel_close_buton = NewPageElement(xpath="//*[@id='addModal']/div[1]/span[2]", describe="关闭按钮")
    add_unit_channel_name = NewPageElement(xpath="//div[@class='modal-scrollable']//td[2]", describe="单位频道名称")
    # 编辑单位频道
    edit_unit_channel_save_buton = NewPageElement(xpath="//div[@id='editModal']//button[@class='btn radius btn-primary']", describe="保存按钮")
    edit_unit_channel_close_buton = NewPageElement(xpath="//*[@id='editModal']/div[1]/span[2]", describe="关闭按钮")
    # 预览单位频道页面
    preview_unit_channel_title = NewPageElement(xpath="//div[@id='previewModal']//h3[@class='single-overflow']", describe="页面标题")
    preview_unit_channel_close_button = NewPageElement(xpath="//div[@id='previewModal']//span[@class='modal-close']", describe="关闭按钮")
    # 查看单位频道页面
    view_unit_channel_name = NewPageElement(xpath="//*[@id='eaChannel']/div/div[1]/div[1]/div/p", describe="频道名称")
    view_unit_channel_close_button = NewPageElement(xpath="//div[@id='viewModal']//span[@class='modal-close']", describe="频道名称")
    # 单位频道选人页面
    unit_channel_chose_user_ok_button = NewPageElement(xpath="//button[@class='btn radius btn-primary i18n']", describe="确定按钮")